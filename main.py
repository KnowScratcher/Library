import ssl
import socket
from dependencies import *
from pydantic import BaseModel
from worker import isbnindex
from routers.api import record, register, info, query, edit
from routers import webpage
from contextlib import asynccontextmanager
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse, JSONResponse, RedirectResponse
from fastapi import Request
from fastapi.middleware.gzip import GZipMiddleware
import fastapi
import sys
sys.path.insert(1, '/*')
sys.path.insert(1, '.')


@asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    await isbnindex.refreshAll()
    print("\033[35mAPPINFO:  \033[0mindex update done")
    print(
        f"\033[35mip: \033[0m{socket.gethostbyname(socket.gethostname())}:8002")
    yield  # !: to not remove

app = fastapi.FastAPI(openapi_url=None, lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware, minimum_size=500, compresslevel=5)
templates = Jinja2Templates(directory="templates")

app.include_router(webpage.router)
app.include_router(record.router)
app.include_router(register.router)
app.include_router(info.router)
app.include_router(query.router)
app.include_router(edit.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002,
                ssl_keyfile='./key.pem', ssl_certfile='./cert.pem', reload=False)
