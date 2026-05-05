from fastapi import APIRouter, Request,Body,Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router_home = APIRouter()
templates = Jinja2Templates(directory="static/templates")


@router_home.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "request": request,
            "msg": "Xin chào Ánh 👋"
        }
    )

