from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# ---

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id:int
    title:str =Field(min_length=3)
    author:str =Field(min_length=1)
    description:str =Field(min_length=3,max_length=100)
    rating:int =Field(gt=0,lt=6)


BOOKS=[
    Book(1,'Computer Science Pro','Setenova','A very nice book!',5),
    Book(2,'Be Fast with FastAPI','Setenova','A great book!',5),
    Book(3,'Master Endpoints','Setenova','An awesome book!',5),
    Book(4,'HP1','Author 1','Book Description',2),
    Book(5,'HP2','Author 2','Book Description',3),
    Book(6,'HP3','Author 3','Book Description',1)
]

# ---

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)



