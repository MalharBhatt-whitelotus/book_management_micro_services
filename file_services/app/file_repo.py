from datetime import datetime

from sqlalchemy import select,Text
from sqlalchemy.ext.asyncio import AsyncSession

from file_services.app.file_model import PdfDetails

async def create_file(
        filename: str,
        stored_filename: str,
        filepath: str,
        file_size: int,
        page_count: int,
        title: str,
        author: str,
        creator: str,
        producer: str,
        content: Text,
        uploaded_at: datetime,
        db: AsyncSession):
    
    file = PdfDetails(
        filename=filename,
        stored_filename=stored_filename,
        filepath=filepath,
        file_size=file_size,
        page_count=page_count,
        title=title,
        author=author,
        creator=creator,
        producer=producer,
        content=content,
        uploaded_at=uploaded_at
    )

    db.add(file)
    await db.commit()
    await db.refresh(file)
    
    return file

async def get_summery(db):
    summery = await db.execute(select(PdfDetails))
    return summery.scalars().all()