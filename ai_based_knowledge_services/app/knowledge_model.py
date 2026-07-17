from sqlalchemy import Column, String, Integer, DateTime, Text

from ai_based_knowledge_services.app.knowledge_database import Base

class KnowledgeModel(Base):
    __tablename__ = "pdf"
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False, index=True, unique=True)
    filepath = Column(String, nullable=False, index=True, unique=True)
    content_type = Column(String, default="pdf")
    uploaded_at = Column(DateTime, nullable=False, index=True)
    owner_id = Column(Integer, nullable=False)

class PdfDetails(Base):
    __tablename__ = "pdf_details"
    id= Column(Integer, primary_key=True)
    filename = Column(String, nullable=False, index=True)
    stored_filename = Column(String)
    filepath = Column(String)
    file_size = Column(Integer)
    page_count = Column(Integer)
    title = Column(String)
    author = Column(String)
    creator = Column(String)
    producer = Column(String)
    content = Column(Text)
    uploaded_at = Column(DateTime)