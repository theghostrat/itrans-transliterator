import argparse
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from docx import Document
import os

def extract_text(itx_path):
    with open(itx_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    content_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('%') or line.startswith('\\') or line.startswith('#'):
            continue
        content_lines.append(line)
    return '\n'.join(content_lines)

def save_txt(text, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

def save_docx(text, filename):
    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(filename)

def main():
    parser = argparse.ArgumentParser(description="ITRANS to Unicode multi-script converter with export options")
    parser.add_argument('input', help="Input .itx file path")
    parser.add_argument('-f', '--formats', nargs='+', default=['txt'], help="Export formats: txt, docx (default: txt)")
    args = parser.parse_args()

    text = extract_text(args.input)

    target_scripts = [
        sanscript.DEVANAGARI,
        sanscript.BENGALI,
        sanscript.GUJARATI,
        sanscript.GURMUKHI,
        sanscript.KANNADA,
        sanscript.MALAYALAM,
        sanscript.ORIYA,
        sanscript.TAMIL,
        sanscript.TELUGU
    ]

    base_name = os.path.splitext(os.path.basename(args.input))[0]

    for script in target_scripts:
        unicode_text = transliterate(text, sanscript.ITRANS, script)
        script_name = script.lower()
        if 'txt' in args.formats:
            txt_file = f"{base_name}_{script_name}.txt"
            save_txt(unicode_text, txt_file)
            print(f"Saved {txt_file}")
        if 'docx' in args.formats:
            docx_file = f"{base_name}_{script_name}.docx"
            save_docx(unicode_text, docx_file)
            print(f"Saved {docx_file}")

if __name__ == "__main__":
    main()