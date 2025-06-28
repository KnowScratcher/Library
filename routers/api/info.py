from fastapi import APIRouter
from dependencies import *
from fastapi.responses import PlainTextResponse, JSONResponse
import requests


router = APIRouter()

@router.get("/api/bookinfo")
async def info(isbn:str):
    r = requests.get(f"https://nbinet3.ncl.edu.tw/search~S10?////frameset&FF=i{isbn}&1%2C1%2C")
    return PlainTextResponse(r.text)

@router.get("/api/collection")
async def queryCollection():
    print(collectionNameIndex)
    return JSONResponse(json.dumps(collectionNameIndex))
    # with open(locationNameIndexPath,"r",encoding="utf-8") as j:
    #     jsn = json.load(j)
    #     return JSONResponse(json.dumps(jsn))