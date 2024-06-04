from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.produto import ProdutoRepositorio
from schemas.produto import Produto

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/produto", response_class=HTMLResponse)
async def get_produto(request: Request):
    return templates.TemplateResponse("/pages/produtos/produto.html", {"request":request, "navItem": "Produto", "urlItem": "produto" })

@router.get("/cadastrar_produto", response_class=HTMLResponse)
async def get_cadastrar_produto(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/produtos/cadastrar_produto.html", {"request":request, "navItem": "Produto", "urlItem": "produto", "fornecedores": fornecedores })

@router.get("/alterar_produto", response_class=HTMLResponse)
async def get_alterar_produto(request: Request):
    return templates.TemplateResponse("/pages/produtos/alterar_produto.html", {"request":request, "navItem": "Produto", "urlItem": "produto" })

@router.post("/cadastrar_produto")
async def post_produto(produto: Produto = Body()):
    produto = ProdutoRepositorio.inserir(produto)
    return {"MSG": produto.id_produto}

@router.get("/obter_produtos")
async def get_produtos():
    produtos = ProdutoRepositorio.obter_todos()
    return {"MSG": produtos}