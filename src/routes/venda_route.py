from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.venda import Venda

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Venda"
URL_ITEM = "venda"

@router.get("/venda", response_class=HTMLResponse)
async def get_venda(request: Request):
    return templates.TemplateResponse("/pages/vendas/venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })


@router.get("/cadastrar_venda", response_class=HTMLResponse)
async def get_cadastrar_venda(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/cadastrar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })

@router.get("/editar_venda", response_class=HTMLResponse)
async def get_editar_venda(request: Request):
    return templates.TemplateResponse("/pages/vendas/editar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_venda", response_class=HTMLResponse)
async def get_remover_venda(request: Request):
    vendas = VendaRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/remover_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "vendas": vendas })


@router.get("/visualizar_venda", response_class=HTMLResponse)
async def get_visualizar_venda(request: Request):
    vendas = VendaRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/visualizar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "vendas": vendas })

# @router.post("/cadastrar_venda")
# async def post_venda(venda: Vendao = Body()):
#     venda = VendaoRepositorio.inserir(venda)
#     return {"MSG": venda.id_venda}

# @router.get("/obter_vendas")
# async def get_vendas():
#     vendas = VendaoRepositorio.obter_todos()
#     return {"MSG": vendas}
