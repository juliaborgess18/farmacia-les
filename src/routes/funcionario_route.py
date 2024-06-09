from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Funcionário"
URL_ITEM = "funcionario"

@router.get("/funcionario", response_class=HTMLResponse)
async def get_fornecedor(request: Request):
    return templates.TemplateResponse("/pages/funcionario/funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })