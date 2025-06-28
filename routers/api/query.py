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
        for i, j in data.items():
            if index in i or any([index in str(x) for x in j.values()]):
                j["id"] = i
                j["collection"] = collectionNameIndex[isbnIndex[i]]
                res.append(j)
    return {"success": True, "data": res}