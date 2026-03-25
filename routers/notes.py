from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal
from services import ollama_service

router = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@router.post("/",response_model=schemas.Note)
def create_note(note: schemas.NoteCreate ,db: Session = Depends(get_db)):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/", response_model=list[schemas.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notes = db.query(models.Note).offset(skip).limit(limit).all()
    return notes

@router.put("/{note_id}", response_model=schemas.Note)
def update_notes(note_id: int, note_update: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if db_note is None:
        raise HTTPException(status_code=404, detail="Güncellenecek Not Bulunamadı")

    db_note.title = note_update.title
    db_note.content = note_update.content
    db_note.mode = note_update.mode

    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}")
def delete_notes(note_id: int, db: Session = Depends(get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if db_note is None:
        raise HTTPException(status_code=404,detail="Silinecek Not Bulunamadı")

    db.delete(db_note)

    db.commit()

    return {"mesaj": f"{note_id} ID'li not silindi "}




@router.post("/{note_id}/analyze")
def analyze_note(note_id: int, db: Session = Depends(get_db)):

    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()

    if db_note is None:
        raise HTTPException(status_code=404, detail="Not bulunamadı")

    analiz_sonucu = ollama_service.analyze_note_with_llm(
        content=db_note.content,
        mode=db_note.mode
    )
    db_note.analysis = analiz_sonucu
    db.commit()
    db.refresh(db_note)
    return db_note