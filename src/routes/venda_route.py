from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from infrastructure.repositories.funcionario import FuncionarioRepositorio
from infrastructure.repositories.cliente import ClienteRepositorio
from infrastructure.repositories.forma_pagamento import FormaPagamentoRepositorio
from infrastructure.repositories.produto import ProdutoRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.venda import Venda, ProdutoVenda

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Venda"
URL_ITEM = "venda"

@router.get("/venda", response_class=HTMLResponse)
async def get_venda(request: Request):
    return templates.TemplateResponse("/pages/vendas/venda.html", {"request": request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_venda", response_class=HTMLResponse)
async def get_cadastrar_venda(request: Request):
    funcionarios = FuncionarioRepositorio.obter_todos()  # Alteração aqui
    clientes = ClienteRepositorio.obter_todos()
    formas_pagamento = FormaPagamentoRepositorio.obter_todos()
    produtos = ProdutoRepositorio.obter_todos()
    
    # Adicione os prints para verificar os dados
    print("Funcionários:", funcionarios)  # Alteração aqui
    print("Clientes:", clientes)
    print("Formas de Pagamento:", formas_pagamento)
    print("Produtos:", produtos)
    
    return templates.TemplateResponse("/pages/vendas/cadastrar_venda.html", {
        "request": request,
        "navItem": NAV_ITEM,
        "urlItem": URL_ITEM,
        "funcionarios": funcionarios,  # Alteração aqui
        "clientes": clientes,
        "formas_pagamento": formas_pagamento,
        "produtos": produtos
    })

# Outras rotas permanecem sem alteração
