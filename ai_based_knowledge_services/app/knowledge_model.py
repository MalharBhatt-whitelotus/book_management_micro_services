from sqlalchemy import Column, String, Integer, DateTime

from ai_based_knowledge_services.app.knowledge_database import Base

class KnowledgeModel(Base):
    __tablename__ = "pdf"
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False, index=True, unique=True)
    filepath = Column(String, nullable=False, index=True, unique=True)
    content_type = Column(String, default="pdf")
    uploaded_at = Column(DateTime, nullable=False, index=True)
    owner_id = Column(Integer, nullable=False)