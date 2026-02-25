from fastapi import FastAPI

app = FastAPI(title="DevDiary API")
@app.get("/")

def read_root():
    return {"Mesaj": "DevDiary API'ye hoşgeldiniz"}