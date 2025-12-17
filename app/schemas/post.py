from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class AuthorNested(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: AuthorNested

    class Config:
        from_attributes = True
