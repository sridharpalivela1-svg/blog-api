from fastapi import FastAPI
from app.database import engine, Base
import app.models

app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Blog API is running"}
