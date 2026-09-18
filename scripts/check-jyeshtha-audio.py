#!/usr/bin/env python3
"""Su-śrotā Sanskrit-slice decoding; diagnostic evidence, not pronunciation certification."""
import argparse
import io
import json
from pathlib import Path
import re
import tarfile
import unicodedata

import librosa
import numpy as np
import soundfile as sf
import torch
import yaml
import sentencepiece as spm
from hydra.utils import instantiate
from omegaconf import OmegaConf


def load_ctc(checkpoint, device):
    """Load the published encoder and CTC tensors, without unused fork RNNT code."""
    with tarfile.open(checkpoint) as archive:
        def read_suffix(suffix):
            members = [m for m in archive.getmembers() if m.name.endswith(suffix)]
            assert len(members) == 1, (suffix, len(members))
            return archive.extractfile(members[0]).read()
        config = yaml.safe_load(read_suffix('model_config.yaml'))
        state = torch.load(io.BytesIO(read_suffix('model_weights.ckpt')), map_location='cpu', weights_only=True)
        languages = list(config['tokenizer']['langs'])
        assert languages.index('sa') == 16 and len(languages) == 22
        tokenizer_name = config['tokenizer']['langs']['sa']['model_path'].removeprefix('nemo:')
        tokenizer = spm.SentencePieceProcessor(model_proto=read_suffix(tokenizer_name))
        assert tokenizer.get_piece_size() == 256
    decoder_config = dict(config['aux_ctc']['decoder'])
    assert decoder_config.pop('multisoftmax') is True
    assert decoder_config['num_classes'] == 5632
    # Global log-softmax subtracts one scalar per frame. Restricting its output to
    # blank + Sanskrit gives the same argmax as language-specific log-softmax.
    modules = {}
    for name, module_config in [('preprocessor', config['preprocessor']),
                                ('encoder', config['encoder']), ('ctc_decoder', decoder_config)]:
        module = instantiate(OmegaConf.create(module_config))
        prefix = name + '.'
        weights = {k[len(prefix):]: v for k, v in state.items() if k.startswith(prefix)}
        module.load_state_dict(weights, strict=True)
        modules[name] = module.eval().to(device)
    assert modules['ctc_decoder'].state_dict()['decoder_layers.0.weight'].shape[0] == 5633
    return modules, tokenizer


def normalize(text):
    text = unicodedata.normalize('NFC', text)
    return re.sub(r'[\s।॥ऽ\d,.;:|!?]', '', text)


def distance(a, b):
    row = list(range(len(b) + 1))
    for i, left in enumerate(a, 1):
        following = [i]
        for j, right in enumerate(b, 1):
            following.append(min(following[-1] + 1, row[j] + 1, row[j - 1] + (left != right)))
        row = following
    return row[-1]


def main(args):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    modules, tokenizer = load_ctc(args.model, device)
    columns = [5632] + list(range(4096, 4352))

    def greedy(wave):
        signal = torch.tensor(wave, device=device).unsqueeze(0)
        length = torch.tensor([len(wave)], device=device)
        with torch.no_grad():
            features, feature_length = modules['preprocessor'](input_signal=signal, length=length)
            encoded, encoded_length = modules['encoder'](audio_signal=features, length=feature_length)
            logits = modules['ctc_decoder'](encoder_output=encoded)[0][:encoded_length[0]]
            ids = logits[:, columns].argmax(1).cpu().tolist()
        tokens, previous = [], -1
        for index in ids:
            if index != previous and index:
                tokens.append(tokenizer.id_to_piece(index - 1))
            previous = index
        return ''.join(tokens).replace('▁', ' ').strip()

    directory = Path(args.directory)
    results = []
    if args.sample:
        jobs = [(Path(args.sample), json.loads(Path(args.reference).read_text()))]
    else:
        jobs = [(wave, json.loads(wave.with_suffix('.json').read_text())) for wave in sorted((directory / 'units').glob('*.wav'))]
    for wave_path, padas in jobs:
        wave, rate = sf.read(wave_path, dtype='float32')
        if wave.ndim > 1:
            wave = wave.mean(1)
        wave = librosa.resample(wave, orig_sr=rate, target_sr=16000)
        chunks, cursor = [], 0
        # Split long prose in a quiet interval, not at an arbitrary speech boundary.
        while len(wave) - cursor > 16000 * 30:
            candidates = range(cursor + 16000 * 18, cursor + 16000 * 28, 160)
            boundary = min(candidates, key=lambda p: float(np.mean(wave[p:p + 1600] ** 2))) + 800
            chunks.append((cursor, boundary))
            cursor = boundary
        chunks.append((cursor, len(wave)))
        transcript = ' '.join(greedy(wave[start:end]) for start, end in chunks)
        reference = ' '.join(padas)
        reference_chars, transcript_chars = normalize(reference), normalize(transcript)
        cer = distance(reference_chars, transcript_chars) / max(1, len(reference_chars))
        result = {'file': wave_path.name, 'reference': reference, 'transcript': transcript,
                  'cer': round(cer, 5), 'chunkWindows': [[s / 16000, e / 16000] for s, e in chunks],
                  'reviewRequired': True}
        results.append(result)
        Path(args.output).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"ASR {wave_path.name}: diagnostic CER {cer:.1%}\n{transcript}", flush=True)
    print('ASR COMPLETE', len(results), 'units; human pronunciation review remains required', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', required=True)
    parser.add_argument('--directory', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--sample')
    parser.add_argument('--reference')
    main(parser.parse_args())
