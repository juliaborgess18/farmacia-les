from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Devolução"
URL_ITEM = "devolucao"

@router.get("/devolucao", response_class=HTMLResponse)
async def get_devolucao(request: Request):
    return templates.TemplateResponse("/pages/devolucao/devolucao.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })