#!/usr/bin/env python3
"""Extract the exact Tantrasara root text used by the Sarvamula web reader.

The source database is not committed because it contains every work in the
reader. This script writes only the Tantrasara headings and numbered verses to
reader-source.json, preserving the source Devanagari byte-for-byte and using
the reader's own IAST conversion rules.
"""

import argparse
import json
import re
import sqlite3
from pathlib import Path


DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
VERSE_END = re.compile(r"॥\s*([०-९]+)\s*॥")

INDEPENDENT_VOWELS = {
    "अ": "a", "आ": "ā", "इ": "i", "ई": "ī", "उ": "u", "ऊ": "ū",
    "ऋ": "ṛ", "ॠ": "ṝ", "ऌ": "ḷ", "ए": "e", "ऐ": "ai", "ओ": "o", "औ": "au",
}
VOWEL_SIGNS = {
    "ा": "ā", "ि": "i", "ी": "ī", "ु": "u", "ू": "ū", "ृ": "ṛ",
    "े": "e", "ै": "ai", "ो": "o", "ौ": "au",
}
CONSONANTS = {
    "क": "k", "ख": "kh", "ग": "g", "घ": "gh", "ङ": "ṅ", "च": "c", "छ": "ch",
    "ज": "j", "झ": "jh", "ञ": "ñ", "ट": "ṭ", "ठ": "ṭh", "ड": "ḍ", "ढ": "ḍh",
    "ण": "ṇ", "त": "t", "थ": "th", "द": "d", "ध": "dh", "न": "n", "प": "p",
    "फ": "ph", "ब": "b", "भ": "bh", "म": "m", "य": "y", "र": "r", "ल": "l",
    "व": "v", "श": "ś", "ष": "ṣ", "स": "s", "ह": "h", "ळ": "ḷ",
}


def to_iast(text):
    """Python port of BhagDisplay.toIast from sarvamulavani.com/normalize.js."""
    out = []
    pending = False
    for char in text:
        if char in CONSONANTS:
            if pending:
                out.append("a")
            out.append(CONSONANTS[char])
            pending = True
        elif char in VOWEL_SIGNS:
            out.append(VOWEL_SIGNS[char])
            pending = False
        elif char == "्":
            pending = False
        elif char in INDEPENDENT_VOWELS:
            if pending:
                out.append("a")
                pending = False
            out.append(INDEPENDENT_VOWELS[char])
        elif char in "ंँ":
            if pending:
                out.append("a")
                pending = False
            out.append("ṃ")
        elif char == "ः":
            if pending:
                out.append("a")
                pending = False
            out.append("ḥ")
        elif char in "़‍‌":
            continue
        elif char == "ऽ":
            if pending:
                out.append("a")
                pending = False
            out.append("’")
        elif char in {"॑": "\u0301", "॒": "\u0331", "॓": "\u0300", "॔": "\u030d", "᳚": "\u030b"}:
            if pending:
                out.append("a")
                pending = False
            out.append({"॑": "\u0301", "॒": "\u0331", "॓": "\u0300", "॔": "\u030d", "᳚": "\u030b"}[char])
        elif "०" <= char <= "९":
            if pending:
                out.append("a")
                pending = False
            out.append(str(ord(char) - ord("०")))
        elif char == "।":
            if pending:
                out.append("a")
                pending = False
            out.append("|")
        elif char == "॥":
            if pending:
                out.append("a")
                pending = False
            out.append("||")
        else:
            if pending:
                out.append("a")
                pending = False
            out.append(char)
    if pending:
        out.append("a")
    return "".join(out)


def split_verses(text):
    verses = []
    start = 0
    for match in VERSE_END.finditer(text):
        number = int(match.group(1).translate(DEV_DIGITS))
        devanagari = text[start:match.end()].strip()
        # The live database carries an invocation token before the first verse
        # of some chapters; the attached print export begins with the verse.
        devanagari = re.sub(r"^ॐ॥\s*", "", devanagari)
        # Double brackets are internal critical-edition markup. The attached
        # reader export prints their contents as ordinary Sanskrit text.
        devanagari = devanagari.replace("[[", "").replace("]]", "")
        verses.append({"number": number, "devanagari": devanagari, "iast": to_iast(devanagari)})
        start = match.end()
    return verses, text[start:].strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("database", type=Path)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("reader-source.json"))
    args = parser.parse_args()

    connection = sqlite3.connect(args.database)
    rows = connection.execute(
        "SELECT seq, content_type, text_dev FROM entries "
        "WHERE work='tantrasara_sangraha' ORDER BY seq"
    )
    chapters = []
    chapter = None
    topic = ""
    pending = ""
    pending_topic = ""
    for _, content_type, text in rows:
        if content_type == "Heading1":
            if pending:
                raise ValueError(f"Unnumbered source text at chapter boundary: {pending!r}")
            chapter = {"number": len(chapters) + 1, "title": text, "verses": []}
            chapters.append(chapter)
        elif content_type == "Heading2":
            topic = text
        elif content_type == "Sarvamula":
            if chapter is None:
                raise ValueError("Verse encountered before a chapter heading")
            combined = " ".join(part for part in (pending, text) if part)
            verse_topic = pending_topic or topic
            verses, pending = split_verses(combined)
            for verse in verses:
                verse["topic"] = verse_topic
                chapter["verses"].append(verse)
                verse_topic = topic
            pending_topic = verse_topic if pending else ""

    if pending:
        raise ValueError(f"Unnumbered source text after final verse: {pending!r}")

    expected = [75, 24, 141, 161]
    actual = [len(chapter["verses"]) for chapter in chapters]
    if actual != expected:
        raise ValueError(f"Expected chapter verse counts {expected}, found {actual}")
    args.output.write_text(json.dumps({"chapters": chapters}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output} ({sum(actual)} verses)")


if __name__ == "__main__":
    main()
