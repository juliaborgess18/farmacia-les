from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dto.fornecedor.cadastrar_fornecedor_dto import CadastrarFornecedorDTO
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from schemas.endereco import Endereco
from schemas.fornecedor import Fornecedor
from util.mapper_fornecedor import MapperFornecedor
# from dto.fornecedor.cadastrar_fornecedor_dto import CadastrarFornecedorDTO
# from util.mapper_fornecedor import MapperFornecedor

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Fornecedor"
URL_ITEM = "fornecedor"

@router.get("/fornecedor", response_class=HTMLResponse)
async def get_fornecedor(request: Request):
    return templates.TemplateResponse("/pages/fornecedores/fornecedor.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })


@router.get("/cadastrar_fornecedor", response_class=HTMLResponse)
async def get_cadastrar_fornecedor(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/fornecedores/cadastrar_fornecedor.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })

@router.get("/editar_fornecedor", response_class=HTMLResponse)
async def get_editar_fornecedor(request: Request):
    return templates.TemplateResponse("/pages/fornecedores/editar_fornecedor.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_fornecedor", response_class=HTMLResponse)
async def get_remover_fornecedor(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/fornecedores/remover_fornecedor.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })

@router.get("/visualizar_fornecedor", response_class=HTMLResponse)
async def get_visualizar_fornecedor(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/fornecedores/visualizar_fornecedor.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })


@router.post("/api/cadastrar_fornecedor")
async def post_cadastrar_fornecedor(fornecedor:CadastrarFornecedorDTO = Body()):
    print("2")
    fornecedor_para_cadastrar = MapperFornecedor.cadastrar_fornecedor(fornecedor)
    FornecedorRepositorio.inserir(fornecedor_para_cadastrar)
    return {"MSG": True}

