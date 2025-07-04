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
        request=request, name="home.html", context={"name": lang["home"], "lang":lang})


@router.get("/scan")
async def scanPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="scan.html", context={"name": lang["record_borrow_n_return"], "lang":lang})


@router.get("/register")
async def registerPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html", context={"name": lang["register_book"], "lang":lang})

@router.get("/query")
async def queryPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="query.html", context={"name": lang["record_query"], "lang":lang})

@router.get("/edit")
async def editPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="edit.html", context={"name": lang["edit_record"], "lang":lang})
