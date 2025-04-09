import gradio as gr
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from docx import Document
import tempfile
import os

def extract_text(file_obj):
    if hasattr(file_obj, 'read'):
        content = file_obj.read().decode('utf-8')
    else:
        with open(file_obj.name, 'r', encoding='utf-8') as f:
            content = f.read()
    lines = content.splitlines()
    content_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('%') or line.startswith('\\') or line.startswith('#'):
            continue
        content_lines.append(line)
    return '\n'.join(content_lines)

def save_txt(text, script_name):
    fd, path = tempfile.mkstemp(suffix=f"_{script_name}.txt")
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(text)
    return path

def save_docx(text, script_name):
    path = tempfile.mktemp(suffix=f"_{script_name}.docx")
    doc = Document()
    for line in text.splitlines():
        doc.add_paragraph(line)
    doc.save(path)
    return path

script_options = [
    ("Devanagari", sanscript.DEVANAGARI),
    ("Bengali", sanscript.BENGALI),
    ("Gujarati", sanscript.GUJARATI),
    ("Gurmukhi", sanscript.GURMUKHI),
    ("Kannada", sanscript.KANNADA),
    ("Malayalam", sanscript.MALAYALAM),
    ("Oriya", sanscript.ORIYA),
    ("Tamil", sanscript.TAMIL),
    ("Telugu", sanscript.TELUGU)
]

def transliterate_and_save(file_obj, selected_scripts, export_formats):
    text = extract_text(file_obj)
    download_files = []
    for script_name in selected_scripts:
        script_code = dict(script_options)[script_name]
        unicode_text = transliterate(text, sanscript.ITRANS, script_code)
        if 'txt' in export_formats:
            txt_path = save_txt(unicode_text, script_name.lower())
            download_files.append((f"{script_name} (TXT)", txt_path))
        if 'docx' in export_formats:
            docx_path = save_docx(unicode_text, script_name.lower())
            download_files.append((f"{script_name} (DOCX)", docx_path))
    return [file for _, file in download_files]

iface = gr.Interface(
    fn=transliterate_and_save,
    inputs=[
        gr.File(label="Upload .itx File"),
        gr.CheckboxGroup(
            choices=[name for name, _ in script_options],
            label="Select Target Scripts",
            value=["Devanagari"]
        ),
        gr.CheckboxGroup(
            choices=["txt", "docx"],
            label="Select Export Formats",
            value=["txt"]
        )
    ],
    outputs=gr.Files(label="Download Transliteration Files"),
    title="Indic Transliteration Toolkit",
    description="Upload an ITRANS .itx file, select target scripts and export formats, then download the transliterated files."
)

if __name__ == "__main__":
    iface.launch()