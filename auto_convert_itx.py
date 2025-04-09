from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

INPUT_FILE = 'r01.itx'

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

def main():
    text = extract_text(INPUT_FILE)
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
    for script in target_scripts:
        unicode_text = transliterate(text, sanscript.ITRANS, script)
        output_file = f"r01_{script}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(unicode_text)
        print(f"Saved {output_file}")

if __name__ == "__main__":
    main()