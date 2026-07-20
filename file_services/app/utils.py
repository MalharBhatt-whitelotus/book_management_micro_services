import os
import fitz
import uuid
import shutil
import pymupdf

from fastapi import UploadFile
from file_services.app.file_config import settings

@staticmethod
def save_file(file: UploadFile):
    os.makedirs(settings.UPLOADS_DIR, exist_ok=True)
    filename = f"{uuid.uuid4()}.pdf"
    filepath = os.path.join(settings.UPLOADS_DIR, filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"stored_filename":filename,"filepath":filepath}

@staticmethod
def extract_details(filepath: str):
    doc = fitz.open(filepath)
    metadata = doc.metadata
    return metadata

@staticmethod
def extract_text(file):
    text = ""
    doc = pymupdf.open(file)
    page_count = len(doc)
    for page in doc:
            text += page.get_text()
    return {"text":text,"page_count":page_count}

@staticmethod
def get_file_size(file_path):
     size = os.path.getsize(file_path)
     size_mb = round((1024*1024),2)
     return size_mb