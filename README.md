# ITRANS Indic Transliteration Toolkit

---

## About

**ITRANS Indic Transliteration Toolkit** is a powerful, open-source Python package and CLI tool that converts Sanskrit and Indic language texts written in the ITRANS ASCII scheme into beautiful Unicode text across multiple Brahmic scripts.

Whether you're a linguist, developer, researcher, or enthusiast, this toolkit helps you effortlessly transliterate ancient scriptures, poetry, or modern texts into your preferred Indic script, with support for multiple export formats.

---

## Features

- **Multi-script support:** Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu
- **Multi-format export:** Generate Unicode `.txt` and `.docx` files simultaneously
- **Batch processing:** Convert entire `.itx` documents in one go
- **Easy CLI:** Simple command-line interface with flexible options
- **Open-source & extensible:** MIT licensed, easy to customize

---

## Quick Start

### 1. Install dependencies

```bash
pip install indic-transliteration python-docx
```

### 2. Convert an `.itx` file to Unicode `.txt` and `.docx` files

```bash
python transliterate_cli.py yourfile.itx -f txt docx
```

---

## Why use this toolkit?

- **Save time:** Automate transliteration of large documents
- **Multi-script output:** Reach wider audiences by publishing in multiple scripts
- **Professional output:** Unicode text ready for publishing, printing, or further processing
- **Community-driven:** Built on top of trusted open-source libraries like `indic-transliteration`

---

## Repository Highlights

- `transliterate_cli.py` — Unified CLI tool with multi-format export
- `itrans_parser/` — Custom transliteration engine (optional)
- `.gitignore` — Clean repo without generated files
- `LICENSE` — MIT license for maximum freedom

---

## Contributing

Pull requests, issues, and stars are welcome! Help us improve this toolkit for the Indic language community.

---

## License

MIT License © 2025 sourabh singh / theghostrat

---

## ⭐ If you find this project useful, please star it on GitHub and share with others!