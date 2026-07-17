from pydantic import Field, BaseModel
from datetime import datetime

class PdfUploads(BaseModel):
    filename : str = Field(..., min_length=1, max_length=100)
    stored_filename: str
    filepath: str = Field(...)
    file_size: int = Field(...)
    page_count: int = Field(...)
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    creator: str
    producer: str
    content: str = Field(...)
    uploaded_at: datetime = Field(...)
    
class PdfResponse(BaseModel):
    id: int
    filename : str
    stored_filename: str
    filepath: str
    file_size: int
    page_count: int
    title: str
    author: str
    creator: str
    producer: str
    content: str
    uploaded_at: datetime