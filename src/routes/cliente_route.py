from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Cliente"
URL_ITEM = "cliente"

@router.get("/cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/cadastrar_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/editar_cliente", response_class=HTMLResponse)
async def get_editar_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/editar_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_cliente", response_class=HTMLResponse)
async def get_remover_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/remover_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/visualizar_cliente", response_class=HTMLResponse)
async def get_visualizar_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/visualizar_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })


