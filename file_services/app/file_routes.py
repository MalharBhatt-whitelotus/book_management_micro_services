from fastapi import APIRouter, BackgroundTasks, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import file_services.app.file_service as service
from file_services.app.file_database import get_db
from file_services.app.file_schema import PdfUploads, PdfResponse

router = APIRouter(prefix="/file", tags=["file"])

@router.post("/upload",response_model=PdfResponse)
async def upload_file(background_task : BackgroundTasks, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    file = await service.process_pdf(file, db)
    return file

@router.get("/summerize/{fileID}",response_model=PdfResponse)
async def summerize_doc(fileID: int, db: AsyncSession = Depends(get_db)):
    summery = await service.get_summery(fileID, db)
    return summery

@router.get("/list", response_model=list[PdfResponse])
async def get_file_list(db: AsyncSession = Depends(get_db)):
    return await service.get_file_list(db)

@router.delete("/delete/{file_id}")
async def delete_file_by_id(file_id: int, db: AsyncSession = Depends(get_db)):
    return await service.delete_file_by_id(file_id, db)