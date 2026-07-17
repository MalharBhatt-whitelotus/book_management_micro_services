import os
import fitz
import uuid
import shutil
import pymupdf 
UPLOADS_DIR="ai_based_knowledge_services/uploads"
@staticmethod
def extract_text(file):
    text = ""
    doc = pymupdf.open(file)
    page_count = len(doc)
    for page in doc:
            text += page.get_text()
    return text,page_count

print(extract_text("/Users/maulik/malhar /day-16 task2/Intern2_HighPriority_AI_Microservice.pdf"))

@staticmethod
def extract_details(filepath: str):
    doc = fitz.open(filepath)
    metadata = doc.metadata
    return metadata

print(extract_details("/Users/maulik/malhar /day-16 task2/Intern2_HighPriority_AI_Microservice.pdf"))

@staticmethod
def save_file(file):
    os.makedirs(UPLOADS_DIR, exist_ok=True)
    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(UPLOADS_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"stored_filename":filename,"filepath":filepath}
