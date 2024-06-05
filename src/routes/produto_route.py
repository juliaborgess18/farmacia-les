from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.produto import ProdutoRepositorio
from schemas.produto import Produto

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Produto"
URL_ITEM = "produto"

@router.get("/produto", response_class=HTMLResponse)
async def get_produto(request: Request):
    return templates.TemplateResponse("/pages/produtos/produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_produto", response_class=HTMLResponse)
async def get_cadastrar_produto(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/produtos/cadastrar_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })

@router.get("/editar_produto", response_class=HTMLResponse)
async def get_editar_produto(request: Request):
    return templates.TemplateResponse("/pages/produtos/editar_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_produto", response_class=HTMLResponse)
async def get_remover_produto(request: Request):
    return templates.TemplateResponse("/pages/produtos/remover_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/visualizar_produto", response_class=HTMLResponse)
async def get_editar_produto(request: Request):
    produtos = ProdutoRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/produtos/visualizar_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "produtos": produtos })

@router.post("/cadastrar_produto")
async def post_produto(produto: Produto = Body()):
    produto = ProdutoRepositorio.inserir(produto)
    return {"MSG": produto.id_produto}

@router.get("/obter_produtos")
async def get_produtos():
    produtos = ProdutoRepositorio.obter_todos()
    return {"MSG": produtos}
