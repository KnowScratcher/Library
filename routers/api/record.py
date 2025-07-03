from fastapi import APIRouter
from pydantic import BaseModel
from dependencies import *

router = APIRouter()


class Record(BaseModel):
    id: str


@router.post("/api/record")
async def record(rec: Record):
    searchId = rec.id
    result = isbnIndex.get(searchId, False)
    print(isbnIndex, searchId)
    if not result:
        return {"success": False, "message": "Book not found, please register or rescan."}
    # result = result.get("path", "_")
    collectionName = collectionNameIndex.get(result, False)
    newFile = os.path.join(locationPath,
                           result+".json")  # only one layer
    print(newFile)
    if not os.path.exists(newFile):
        return {"success": False, "message": "Database error."}

    with open(newFile, "r+", encoding="UTF-8") as nf:
        data: dict = json.load(nf)
        bookData = data.get(searchId, False)
        if not bookData:
            return {"success": False, "message": "Book not in database."}
        data[searchId]["isHere"] = not data[searchId]["isHere"]
        nf.seek(0)
        json.dump(data, nf)
        nf.truncate()
        return {"success": True, "name": data[searchId]["name"], "isIn": data[searchId]["isHere"], "collection": collectionName}
