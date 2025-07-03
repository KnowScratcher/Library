from fastapi import APIRouter
from pydantic import BaseModel
from dependencies import *
from worker import locationName, isbnindex, shelver

router = APIRouter()


class Book(BaseModel):
    """Book model

    Args:
        id (str): the isbn of the book
        isbn (str): the isbn of the book
        name (str): the name of the book
        collection (str): the collection of the book
        collectionName (str): the name of the collection of the book
    """
    id: str
    isbn: str
    name: str
    collection: str
    collectionName: str


async def checkIsbnInfo(id: str) -> bool:
    """check if the id has been registered before

    Args:
        id (str): the isbn of the book

    Returns:
        bool: `True`: not registered before, `False`: registered before
    """
    return not (id in isbnIndex)


@router.post("/api/register")
async def register(book: Book):
    # print(book.id)
    if not await checkIsbnInfo(book.id):  # check if the book is registered
        return {"success": False, "message": "Book has been registered!"}
    if not book.collection in collectionNameIndex:  # check whether to register a new collection
        if not await locationName.registerLocation(book.collection, book.collectionName):
            return {"success": False, "message": "Collection register failed."}
    await isbnindex.set(book.id, book.collection)
    await shelver.add(book.collection, book.id, book.isbn, book.name)
    return {"success": True, "collection": book.collection, "collectionName": book.collectionName, "id": book.id, "name": book.name}

@router.get("/api/available")
async def available(id: str):
    if not await checkIsbnInfo(id):  # check if the book is registered
        print("in")
        return {"success": False, "message": "Book has been registered!"}
    else:
        print("out")
        return {"success": True}