from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
import json
import os
from dependencies import basePath

templates = Jinja2Templates(directory="templates")
router = APIRouter()

with open(os.path.join(basePath, "config.json"), "r", encoding="UTF-8") as f:
    config = json.load(f)

with open(os.path.join(basePath, "lang", f"{config['lang']}.json"), "r", encoding="UTF-8") as f:
    lang = json.load(f)

@router.get("/")
async def homePage(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"name": "首頁", "lang":lang})


@router.get("/scan")
async def scanPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="scan.html", context={"name": "出入紀錄", "lang":lang})


@router.get("/register")
async def registerPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html", context={"name": "登錄圖書", "lang":lang})

@router.get("/query")
async def queryPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="query.html", context={"name": "紀錄查詢", "lang":lang})
