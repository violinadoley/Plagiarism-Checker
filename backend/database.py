from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class ResearchPaper(Base):
    __tablename__ = "research_papers"

    id = Column(Integer, primary_key=True, index=True)
    abstract = Column(Text)
    articleNumber = Column(String)
    articleTitle = Column(String)
    doi = Column(String)
    publicationTitle = Column(String)
    publicationYear = Column(String)
    volume = Column(String)
    issue = Column(String)
    documentLink = Column(String)
    xml = Column(Text)

Base.metadata.create_all(bind=engine)
