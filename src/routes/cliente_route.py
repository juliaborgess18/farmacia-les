from fastapi import APIRouter, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dto.endereco.endereco import AlterarEnderecoDTO
from infrastructure.config.database import SessionLocal
from schemas.cliente import Cliente
from infrastructure.repositories.cliente import ClienteRepositorio
from dto.cliente.cliente import AlterarClienteDTO, CadastrarClienteDTO
from util.Mappers.cliente.mapper_cliente import MapperCliente

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Cliente"
URL_ITEM = "cliente"

@router.get("/cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):   
    return templates.TemplateResponse("/pages/clientes/cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_cliente", response_class=HTMLResponse)
async def get_cliente(request: Request):
    return templates.TemplateResponse("/pages/clientes/cadastrar_cliente.html", 
        {"request":request, 
         "funcItem": "Cadastrar", 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM
        })

@router.post("/api/cadastrar_cliente")
async def post_cliente(cliente: CadastrarClienteDTO = Body()):
    cliente_para_cadastrar = MapperCliente.cadastrar_cliente(cliente)
    ClienteRepositorio.inserir(cliente_para_cadastrar)
    return {'MSG': True}

@router.get("/editar_cliente", response_class=HTMLResponse)
async def get_editar_cliente(request: Request, id_cliente: int = 0):
    cliente_para_alterar = ClienteRepositorio.obter_por_id(id_cliente)
    return templates.TemplateResponse("/pages/clientes/editar_cliente.html", 
        {"request":request, 
         "funcItem": "Editar", 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM, 
         "cliente":cliente_para_alterar})

@router.put("/api/editar_cliente")
async def put_editar_cliente(cliente_alterado: AlterarClienteDTO):
    cliente = MapperCliente.alterar_cliente(cliente_alterado)
    ClienteRepositorio.alterar(cliente)
    return {"MSG": True}

@router.get("/remover_cliente", response_class=HTMLResponse)
async def get_remover_cliente(request: Request, id_cliente: int = 0):
    cliente = None
    if id_cliente != 0:
        cliente = ClienteRepositorio.obter_por_id(id_cliente)  
    return templates.TemplateResponse("/pages/clientes/remover_cliente.html", 
        {"request":request, 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM, 
         "cliente":cliente}
    )

@router.delete("/api/remover_cliente")
async def remover_cliente(id_cliente: int = 0):
    ClienteRepositorio.remover(id_cliente)
    return {"MSG": True}

@router.get("/visualizar_cliente", response_class=HTMLResponse)
async def get_visualizar_cliente(request: Request):
    clientes = ClienteRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/clientes/visualizar_cliente.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "clientes": clientes })


