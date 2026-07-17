from pydantic import Field
from ai_based_knowledge_services.app.knowledge_model import KnowledgeModel

class PdfUploads:
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
    uploaded_at: str = Field(...)
class PdfUploads:
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
    uploaded_at: str