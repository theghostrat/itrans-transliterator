# ITRANS Indic Transliteration Toolkit

## Overview
A Python-based toolkit to convert ITRANS-encoded Sanskrit and Indic language texts into Unicode for multiple Brahmic scripts. Supports batch conversion of `.itx` files from sources like sanskritdocuments.org.

---

## Features
- Converts ITRANS ASCII text to Unicode
- Supports Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu
- Batch conversion of `.itx` files to `.txt` and `.docx` files in all supported scripts
- Unified CLI tool with multi-format export options
- Converts Unicode `.txt` files to `.docx` Word documents
- CLI and script-based usage

---

## Dependencies
- Python 3.7+
- [indic-transliteration](https://github.com/sanskrit-coders/indic-transliteration)
- python-docx

Install dependencies with:

```bash
pip install indic-transliteration python-docx
```

---

## Usage

### Unified CLI Tool

Convert an `.itx` file to Unicode `.txt` and/or `.docx` files in all supported scripts:

```bash
python transliterate_cli.py input.itx -f txt docx
```

- `-f` or `--formats` accepts one or more formats: `txt`, `docx`
- Default format is `txt` if not specified

**Example:**

```bash
python transliterate_cli.py r01.itx -f txt docx
```

This generates:

```
r01_devanagari.txt, r01_devanagari.docx
r01_bengali.txt, r01_bengali.docx
...
r01_telugu.txt, r01_telugu.docx
```

---

## Project Structure

```
itrans_parser/          # Custom transliteration engine (optional, superseded by indic-transliteration)
transliterate_cli.py    # Unified CLI tool with multi-format export
auto_convert_itx.py     # Batch convert .itx to Unicode .txt (legacy)
convert_itx.py          # Legacy converter using custom mappings
txt_to_docx.py          # Convert Unicode .txt to .docx
PLAN.md                 # Architectural plan
README.md               # This file
r01.itx                 # Sample input file
```

---

## Credits
- [indic-transliteration](https://github.com/sanskrit-coders/indic-transliteration) for robust script conversion
- Sanskrit Documents project for source `.itx` files

---

## License
MIT License