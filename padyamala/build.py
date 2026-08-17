#!/usr/bin/env python3
"""Build the complete Padyamala reader from its audited IAST/English table."""

from pathlib import Path
import html

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "source.tsv"


def esc(value):
    return html.escape(value, quote=True)


def formatted(value):
    return esc(value).replace(" । ", " ।<br>").replace(" | ", " |<br>")


def records():
    result = []
    for line_number, raw in enumerate(SOURCE.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        parts = raw.split("\t")
        if len(parts) != 3:
            raise ValueError(f"Expected three tab-separated fields on source line {line_number}")
        key, iast, meaning = parts
        result.append({
            "key": key,
            "iast": iast,
            "kannada": transliterate(iast, sanscript.IAST, sanscript.KANNADA),
            "meaning": meaning,
            "numbered": key.isdigit(),
        })
    numbered = [record for record in result if record["numbered"]]
    closing = [record for record in result if not record["numbered"]]
    if [int(record["key"]) for record in numbered] != list(range(1, 123)):
        raise ValueError("The numbered source must contain verses 1 through 122 exactly once and in order")
    if [record["key"] for record in closing] != ["COL1", "COL2", "COL3", "COL4"]:
        raise ValueError("The four closing source units are missing or out of order")
    if any(not record["iast"].strip() or not record["meaning"].strip() for record in result):
        raise ValueError("Every source unit must have IAST and a complete English meaning")
    return result


def article(record):
    if record["numbered"]:
        label = f'Verse {record["key"]}'
        identifier = f'verse-{record["key"]}'
        class_name = "text-unit verse"
        number = f'<div class="verse-number">{record["key"]}</div>'
    else:
        labels = {"COL1": "Authorship colophon", "COL2": "Concluding colophon", "COL3": "Dedication", "COL4": "Closing prayer"}
        label = labels[record["key"]]
        identifier = record["key"].lower()
        class_name = "text-unit closing"
        number = ""
    search = " ".join((label, record["kannada"], record["iast"], record["meaning"])).lower()
    return f'''<article class="{class_name}" id="{identifier}" data-search="{esc(search)}">
<div class="unit-label">{label}</div>
<div class="source">{number}<div class="kannada">{formatted(record["kannada"])}</div><div class="iast">{formatted(record["iast"])}</div></div>
<div class="meaning"><span>Complete literal English meaning</span>{esc(record["meaning"])}</div>
</article>'''


def main():
    data = records()
    numbered = [record for record in data if record["numbered"]]
    closing = [record for record in data if not record["numbered"]]
    page = [HEAD, COVER, '<section class="reader" id="verses"><h2>Numbered verses</h2>']
    page.extend(article(record) for record in numbered)
    page.append('</section><section class="reader closing-section" id="closing"><h2>Colophon and closing prayers</h2>')
    page.extend(article(record) for record in closing)
    page.extend(('</section>', FOOT))
    (BASE / "index.html").write_text("\n".join(page), encoding="utf-8")
    print("wrote index.html: 122 numbered verses and 4 closing units")


HEAD = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The complete 122-verse Padyamala of Sri Jayatirtha in Kannada script and IAST, with literal English meaning for every verse.">
<title>Padyamālā — Complete Literal English Meaning</title>
<style>
:root{--paper:#fbf6ec;--card:#fffdf8;--ink:#2c2418;--muted:#776a55;--red:#8b2f18;--line:#e5d8c0;--gold:#b58a34}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,"Times New Roman",serif;line-height:1.6}
.site-nav{position:sticky;top:0;z-index:10;display:flex;gap:15px;align-items:center;justify-content:center;flex-wrap:wrap;padding:10px 16px;background:rgba(255,253,248,.97);border-bottom:1px solid var(--line);backdrop-filter:blur(8px)}
.site-nav a{color:var(--red);font:600 13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;text-decoration:none}.site-nav a:hover{text-decoration:underline}
.shell{max-width:960px;margin:0 auto;background:var(--card);min-height:100vh;padding:0 38px 70px;box-shadow:0 8px 30px rgba(72,42,12,.08)}
.cover{text-align:center;padding:70px 10px 40px;border-bottom:1px solid var(--line)}.cover .kn-title{font-family:"Noto Serif Kannada","Kannada Sangam MN",serif;font-size:38px;color:var(--red)}
.cover h1{font-size:32px;margin:10px 0 6px}.cover .byline{font-style:italic;color:#51483a}.cover .promise{max-width:760px;margin:28px auto 12px;font-size:18px}.cover .source-note{max-width:790px;margin:17px auto 0;color:var(--muted);font-size:14px}
.toolbar{position:sticky;top:43px;z-index:8;display:flex;align-items:center;gap:12px;padding:13px 0;background:var(--card);border-bottom:1px solid var(--line)}
.toolbar input{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:#fff;font:15px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.count{white-space:nowrap;color:var(--muted);font:13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
.reader{padding-top:34px}.reader>h2{text-align:center;color:var(--red);font-size:26px;margin:0 0 25px}.closing-section{border-top:1px solid var(--line);margin-top:42px;padding-top:42px}
.text-unit{margin:0 0 24px;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 2px 10px rgba(72,42,12,.04)}.unit-label{padding:8px 14px;background:#f4ead8;color:var(--red);font:700 12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.35px;text-transform:uppercase}
.source{position:relative;padding:18px 20px 17px;background:#fbf8f1;border-bottom:1px solid #eee4d2}.verse-number{position:absolute;right:14px;top:12px;color:#aa9a7d;font:12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.kannada{font-family:"Noto Serif Kannada","Kannada Sangam MN",serif;font-size:20px;line-height:1.9;padding-right:36px}.iast{font-size:16px;font-style:italic;color:#655a4c;margin-top:9px;line-height:1.65;padding-right:36px}
.meaning{padding:17px 20px;font-size:16px}.meaning>span{display:block;margin-bottom:7px;color:var(--red);font:700 12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;letter-spacing:.45px;text-transform:uppercase}
footer{text-align:center;color:var(--muted);font-size:13px;padding:38px 0 0}.hidden{display:none!important}
@media(max-width:680px){.shell{padding:0 14px 45px;box-shadow:none}.site-nav{gap:11px}.toolbar{top:43px}.cover{padding:42px 4px 30px}.cover .kn-title{font-size:30px}.cover h1{font-size:26px}.kannada{font-size:18px;padding-right:25px}.iast{font-size:15px;padding-right:25px}.source,.meaning{padding-left:15px;padding-right:15px}}
@media print{body{background:#fff}.site-nav,.toolbar{display:none}.shell{max-width:none;padding:0;box-shadow:none}.text-unit{break-inside:avoid;box-shadow:none}.cover{break-after:page}}
</style></head><body>
<nav class="site-nav" aria-label="Reader navigation"><a href="../index.html">← All guides</a><a href="#verses">122 verses</a><a href="#closing">Closing text</a></nav>
<main class="shell">'''

COVER = '''<section class="cover">
<div class="kn-title">॥ ಪದ್ಯಮಾಲಾ ॥</div>
<h1>Padyamālā</h1>
<div class="byline">of Śrī Jayatīrtha</div>
<p class="promise">All 122 numbered Sanskrit verses in the source’s Kannada script, with normalized IAST and a complete literal English meaning that accounts for every word without summarization.</p>
<p class="source-note">The <a href="https://srimadhvyasa.wordpress.com/wp-content/uploads/2013/02/padhyamala12022013.pdf">source PDF</a> is Sanskrit printed in Kannada script. Its authorship colophon, concluding colophon, dedication, and final prayer are preserved after the numbered verses. Named Vedic passages are translated as the text presents them—as references by their opening words—without silently inserting the full external hymns.</p>
</section>
<div class="toolbar"><input id="search" type="search" placeholder="Search Kannada, IAST, or English meaning…" aria-label="Search the Padyamala"><span class="count" id="count">122 verses + 4 closing items</span></div>'''

FOOT = '''<footer>Source-complete study edition · 122 numbered verses plus all closing text · no abridgment</footer>
</main>
<script>
(function(){
 const input=document.getElementById('search'),units=[...document.querySelectorAll('.text-unit')],count=document.getElementById('count');
 input.addEventListener('input',()=>{const q=input.value.trim().toLowerCase();let verses=0,closing=0;units.forEach(unit=>{const show=!q||unit.dataset.search.includes(q);unit.classList.toggle('hidden',!show);if(show){unit.classList.contains('verse')?verses++:closing++}});count.textContent=q?verses+' verses + '+closing+' closing items':'122 verses + 4 closing items'});
})();
</script></body></html>'''


if __name__ == "__main__":
    main()
