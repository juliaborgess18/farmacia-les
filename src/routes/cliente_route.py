from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from infrastructure.config.database import SessionLocal
from schemas.cliente import Cliente
from infrastructure.repositories.cliente import ClienteRepositorio

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Cliente"
URL_ITEM = "cliente"

@router.get("/cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):   
    return templates.TemplateResponse("/pages/clientes/cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/cadastrar_cliente.html", {"request":request, "funcItem": "Cadastrar", "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/editar_cliente", response_class=HTMLResponse)
async def get_editar_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/editar_cliente.html", {"request":request, "funcItem": "Editar", "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_cliente", response_class=HTMLResponse)
async def get_remover_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/remover_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/visualizar_cliente", response_class=HTMLResponse)
async def get_visualizar_cliente(request: Request):
    clientes = ClienteRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/clientes/visualizar_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "clientes": clientes })

# ENDPOINTS PARA O BANCO DE DADOS
@router.post("/cadastrar_cliente")
async def post_cliente(cliente: Cliente = Body()):
    cliente = ClienteRepositorio.inserir(cliente)
    return {'MSG':cliente.id_cliente}


