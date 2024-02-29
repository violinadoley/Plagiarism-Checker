from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
import shutil
import os
from typing import List
from database import SessionLocal, engine, ResearchPaper

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class PlagiarismScore(BaseModel):
    plagiarism_score: float

@app.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        with open(file.filename, "wb") as temp_file:
            shutil.copyfileobj(file.file, temp_file)
        file_content = open(file.filename).read()
        matching_papers = db.query(ResearchPaper).filter(ResearchPaper.abstract == file_content).all()

        plagiarism_percentage = len(matching_papers) / db.query(ResearchPaper).count() * 100
        os.remove(file.filename)
        return JSONResponse(content={"plagiarism_score": plagiarism_percentage})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
