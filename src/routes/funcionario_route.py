from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Funcionário"
URL_ITEM = "funcionario"

@router.get("/funcionario", response_class=HTMLResponse)
async def get_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_funcionario", response_class=HTMLResponse)
async def get_cadastrar_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/cadastrar_funcionario.html", {"request":request, "funcItem": "Cadastrar", "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/editar_funcionario", response_class=HTMLResponse)
async def get_editar_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/editar_funcionario.html", {"request":request, "funcItem": "Editar", "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_funcionario", response_class=HTMLResponse)
async def get_remover_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/remover_funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/visualizar_funcionario", response_class=HTMLResponse)
async def get_visualizar_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/visualizar_funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })