from docx import Document

def txt_to_docx(txt_path, docx_path):
    doc = Document()
    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            doc.add_paragraph(line.rstrip())
    doc.save(docx_path)
    print(f"Saved {docx_path}")

if __name__ == "__main__":
    txt_file = 'r01_Devanagari.txt'
    docx_file = 'r01_Devanagari.docx'
    txt_to_docx(txt_file, docx_file)