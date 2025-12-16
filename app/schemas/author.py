from pydantic import BaseModel, EmailStr

class AuthorCreate(BaseModel):
    name: str
    email: EmailStr

class AuthorUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class AuthorResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
