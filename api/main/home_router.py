from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["메인 페이지"])

templates = Jinja2Templates(directory="./templates/main")

@router.get("/test", response_class=HTMLResponse)
async def testRouter(request: Request):
    return templates.TemplateResponse(name="test.html", request=request)

@router.get("/GNU_PIESTA/home", response_class=HTMLResponse)
async def getHome(request: Request):
    return templates.TemplateResponse(name="home.html", request=request)
