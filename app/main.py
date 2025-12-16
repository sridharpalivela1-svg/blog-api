from fastapi import FastAPI
from app.database import engine, Base
import app.models
from app.routes.author import router as author_router

app = FastAPI(title="Blog API")

Base.metadata.create_all(bind=engine)

app.include_router(author_router)

@app.get("/")
def root():
    return {"message": "Blog API is running"}
