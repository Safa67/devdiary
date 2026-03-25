from fastapi import FastAPI
import models
from database import engine
from routers import notes
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevDiary API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Tüm adreslere izin ver (Geliştirme aşaması için)
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes.router)
@app.get("/")

def read_root():
    return {"Mesaj": "DevDiary API'ye hoşgeldiniz"}

