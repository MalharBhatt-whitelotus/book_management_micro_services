from fastapi import APIRouter, BackgroundTasks, HTTPException, status, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ai_based_knowledge_services.app.knowledge_database import get_db
import ai_based_knowledge_services.app.knowledge_service as service
from ai_based_knowledge_services.app.knowledge_schema import PdfUploads, PdfResponse

router = APIRouter(prefix="/ai", tags=["ai"])

@router.post("/upload",response_model=PdfResponse)
async def upload_file(background_task : BackgroundTasks, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    file = await service.process_pdf(file, db)
    return file

@router.get("/summerize",response_model=list[PdfResponse])
async def summerize_doc(db: AsyncSession = Depends(get_db)):
    summery = await service.get_summery(db)
    return summery

@router.get("/ask")
async def ask(query: str, db: AsyncSession = Depends(get_db)):
    response = await service.ask_query(query, db)
    return response