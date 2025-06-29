from fastapi import APIRouter
from pydantic import BaseModel
from dependencies import *
from worker import locationName, isbnindex, shelver
import os

router = APIRouter()


@router.get("/api/query")
async def query(index: str):
    res = []
    for i in os.listdir(locationPath):
        data:dict = json.load(open(os.path.join(locationPath, i), "r", encoding="UTF-8"))
        for k, j in data.items(): # overwrite i to key
            if index in k or index in i or index in collectionNameIndex[i[:-5]] or any([all([index_s in str(x) for index_s in index.split(" ")]) for x in j.values()]):
                j["id"] = k
                j["collection"] = collectionNameIndex[isbnIndex[k]]
                res.append(j)
    return {"success": True, "data": res}