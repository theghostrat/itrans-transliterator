# ITRANS Indic Transliteration Toolkit

---

## About

**ITRANS Indic Transliteration Toolkit** is a powerful, open-source Python package with a modern **Gradio web interface** to convert Sanskrit and Indic language texts written in the ITRANS ASCII scheme into beautiful Unicode text across multiple Brahmic scripts.

Whether you're a linguist, developer, researcher, or enthusiast, this toolkit helps you effortlessly transliterate ancient scriptures, poetry, or modern texts into your preferred Indic script, with support for multiple export formats.

---

## Features

- **Interactive Gradio Web UI**: Upload `.itx` files, select scripts and formats, and download results instantly
- **Multi-script support**: Devanagari, Bengali, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Tamil, Telugu
- **Multi-format export**: Unicode `.txt` and `.docx` files
- **Batch processing**: Convert entire `.itx` documents in one go
- **Open-source & extensible**: MIT licensed, easy to customize

---

## Quick Start

### 1. Install dependencies

```bash
pip install indic-transliteration python-docx gradio
```

### 2. Launch the Gradio Web App

```bash
python gradio_app.py
```

Then open the provided local URL (e.g., `http://127.0.0.1:7860`) in your browser.

---

## Why use this toolkit?

- **Save time:** Automate transliteration of large documents
- **Multi-script output:** Reach wider audiences by publishing in multiple scripts
- **Professional output:** Unicode text ready for publishing, printing, or further processing
- **User-friendly:** No coding required, just use the web interface

---

## Repository Highlights

- `gradio_app.py` — Interactive web UI with file upload, script/format selection, and downloads
- `transliterate_cli.py` — CLI tool with multi-format export (optional)
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