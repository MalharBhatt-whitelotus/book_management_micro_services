from datetime import datetime
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

import file_services.app.utils as utils
import file_services.app.file_repo as repo
# from file_services.app.ai.ai_service import AIService

async def process_pdf(file: UploadFile, db: AsyncSession):
    # save file
   file_detail = utils.save_file(file)
   
   if file_detail:
        # extract metadata
        file_metadata = utils.extract_details(file_detail["filepath"])
        file_size = utils.get_file_size(file_detail["filepath"])
        uploaded_at = datetime.now()
        # extract text
        content = utils.extract_text(file_detail["filepath"])
        filename = file.filename

        # save database
        file = await repo.create_file(
            filename, 
            file_detail["stored_filename"], 
            file_detail["filepath"], 
            file_size, content["page_count"],
            file_metadata["title"], 
            file_metadata["author"], 
            file_metadata["creator"],
            file_metadata["producer"],
            content["text"],
            uploaded_at,
            db)
        
        return file
   
async def get_summery(db):
       summery = await repo.get_summery(db)
       return summery

# async def ask_query(query: str, db: AsyncSession):
#     pdfs = await get_summery(db)

#     context = ""

#     for pdf in pdfs:
#         context += f"""
# Document ID: {pdf.id}
# Filename: {pdf.filename}
# Stored Filename: {pdf.stored_filename}
# File Path: {pdf.filepath}
# File Size: {pdf.file_size} bytes
# Page Count: {pdf.page_count}
# Title: {pdf.title}
# Author: {pdf.author}
# Creator: {pdf.creator}
# Producer: {pdf.producer}
# Uploaded At: {pdf.uploaded_at}

# Content:
# {pdf.content}

# ==================================================
# """

#     response = await AIService.ask_query(query, context)

#     return {"response": response}