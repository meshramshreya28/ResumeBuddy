import PyPDF2
from docx import Document


def extract_text(filepath):

    text = ''

    # Read PDF files
    if filepath.endswith('.pdf'):

        with open(filepath, 'rb') as file:

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted

    # Read DOCX files
    elif filepath.endswith('.docx'):

        doc = Document(filepath)

        for para in doc.paragraphs:
            text += para.text + '\n'

    return text.lower()