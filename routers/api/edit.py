from fastapi import APIRouter
from dependencies import *
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
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

class Books(BaseModel):
    """Book model

    Args:
        id (str): the isbn of the book
        isbn (str): the isbn of the book
        name (str): the name of the book
        collection (str): the collection of the book
        collectionName (str): the name of the collection of the book
    """
    ids: list[str]
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

@router.post("/api/edit_one")
async def edit_one(book: Book):
    if await checkIsbnInfo(book.id):  # check if the book is registered
        return {"success": False, "message": "Book has not been registered!"}
    if not book.collection in collectionNameIndex:  # check whether to register a new collection
        if not await locationName.registerLocation(book.collection, book.collectionName):
            return {"success": False, "message": "Collection register failed."}
    await shelver.remove(isbnIndex[book.id], book.id)
    await isbnindex.set(book.id, book.collection)
    await shelver.add(book.collection, book.id, book.isbn, book.name)
    return {"success": True, "collection": book.collection, "collectionName": book.collectionName, "id": book.id, "name": book.name}

@router.post("/api/edit_lot")
async def edit_lot(book: Books):
    if not book.collection in collectionNameIndex:  # check whether to register a new collection
        if not await locationName.registerLocation(book.collection, book.collectionName):
            return {"success": False, "message": "Collection register failed."}
    for id in book.ids:
        if await checkIsbnInfo(id):  # check if the book is registered
            return {"success": False, "message": "Book has not been registered!"}
        with open(os.path.join(locationPath, isbnIndex[id]+".json"), "r", encoding="utf-8") as j:
            jsn = json.load(j)
            dat = jsn[id]
        await shelver.remove(isbnIndex[id], id)
        await isbnindex.set(id, book.collection)
        await shelver.add(book.collection, id, dat.get("ISBN", ""), dat.get("name", ""))
    return {"success": True, "collection": book.collection, "collectionName": book.collectionName}