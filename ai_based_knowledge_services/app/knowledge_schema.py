from pydantic import Field
from ai_based_knowledge_services.app.knowledge_model import KnowledgeModel

class KnowledgeRequest:
    filename: str = Field(..., min_length=1, max_length=100)
    filepath: str = Field(..., min_length=1, max_length=100)
    content_type: str = Field(..., default="pdf", min_length=1,max_length=10)
    uploaded_at: str = Field(...)
    ower_id: int = Field(...)

class KnowledgeResponse:
    id: int 
    filename: str
    filepath: str
    content_type: str
    uploaded_at: str
    ower_id: int

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