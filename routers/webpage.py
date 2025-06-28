from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
async def homePage(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html", context={"name": "首頁"})


@router.get("/scan")
async def scanPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="scan.html", context={"name": "出入紀錄"})


@router.get("/register")
async def registerPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="register.html", context={"name": "登錄圖書"})

@router.get("/query")
async def queryPage(request: Request):
    return templates.TemplateResponse(
        request=request, name="query.html", context={"name": "紀錄查詢"})
