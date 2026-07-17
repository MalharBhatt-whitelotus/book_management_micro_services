from pydantic import Field
from datetime import datetime
from ai_based_knowledge_services.app.knowledge_model import KnowledgeModel

class KnowledgeRequest:
    id: int = Field(...)
    filename: str = Field(..., min_length=1, max_length=100)
    filepath: str = Field(..., min_length=1, max_length=100)
    content_type: str = Field(..., default="pdf", min_length=1,max_length=10)
    uploaded_at: datetime = Field(...)
    ower_id: int = Field(...)