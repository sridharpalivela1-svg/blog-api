from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routes.author import router as author_router

app = FastAPI(title="Blog API")

# CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)

# REGISTER ROUTERS
app.include_router(author_router)

@app.get("/")
def root():
    return {"message": "Blog API is running"}

