import streamlit as st
import re
from docx import Document
import PyPDF2

st.set_page_config(page_title="Advanced Word Counter")

st.title("📂 Word Counter (TXT, DOCX, PDF)")

uploaded_file = st.file_uploader(
    "Upload file", type=["txt", "docx", "pdf"]
)

def extract_text(file):
    file_type = file.name.split(".")[-1]

    if file_type == "txt":
        return file.read().decode("utf-8")

    elif file_type == "docx":
        doc = Document(file)
        return " ".join([para.text for para in doc.paragraphs])

    elif file_type == "pdf":
        pdf = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

    else:
        return ""

if uploaded_file is not None:
    text = extract_text(uploaded_file).lower()

    # Clean text
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    st.subheader("📊 Word Frequencies")

    for word in sorted(word_count):
        st.write(f"{word}: {word_count[word]}")

    # 🔥 Extra Features
    st.write(f"📌 Total Words: {len(words)}")

    if word_count:
        most = max(word_count, key=word_count.get)
        st.write(f"🔥 Most Frequent Word: {most}")
