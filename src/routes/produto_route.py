from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter, Body, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dto.produto.cadastrar_produto_dto import CadastrarProdutoDTO
from dto.produto.editar_produto_dto import EditarProdutoDTO
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.produto import ProdutoRepositorio
from schemas.produto import Produto
from util.mapper import Mapper

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
async def get_editar_produto(request: Request, id_produto: int = 0):
    produto = ProdutoRepositorio.obter_por_id(id_produto) if id_produto is not 0 else None
    return templates.TemplateResponse("/pages/produtos/editar_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "produto": produto })

@router.get("/remover_produto", response_class=HTMLResponse)
async def get_remover_produto(request: Request, id_produto: int = 0):
    produto = ProdutoRepositorio.obter_por_id(id_produto) if id_produto is not 0 else None
    return templates.TemplateResponse("/pages/produtos/remover_produto.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "produto": produto })

@router.get("/visualizar_produto", response_class=HTMLResponse)
async def visualizar_produto(   request: Request,
                                nome: Optional[str] = Query("", alias="nome"),
                                data_inicio: Optional[str] = Query(None, alias="data_inicio"),
                                data_final: Optional[str] = Query(None, alias="data_final"),
                                valor_min: Optional[str] = Query(None, alias="valor_min"),
                                valor_max: Optional[str] = Query(None, alias="valor_max")):
    
    parse_data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date() if not (data_inicio == None or data_inicio == '') else date.min
    parse_data_final = datetime.strptime(data_final, "%Y-%m-%d").date() if not (data_final == None or data_final == '') else date.max

    parse_valor_min = float(valor_min) if not (valor_min == None or valor_min == '') else 0
    parse_valor_max = float(valor_max) if not (valor_max == None or valor_max == '') else float('inf')

    produtos = ProdutoRepositorio.obter_com_filtros(nome, parse_data_inicio, parse_data_final, parse_valor_min, parse_valor_max)
    return templates.TemplateResponse("/pages/produtos/visualizar_produto.html", {
        "request":request, 
        "navItem": NAV_ITEM, 
        "urlItem": URL_ITEM, 
        "produtos": produtos, 
        "nome": nome,
        "data_inicio": data_inicio,
        "data_final": data_final,
        "valor_min": valor_min,
        "valor_max": valor_max})


@router.post("/api/cadastrar_produto")
async def post_produto(produto: CadastrarProdutoDTO = Body()):
    produto_mapeado = Mapper.MapperProduto.mapear_cadastrar_produto_dto(produto)
    produto_inserido = ProdutoRepositorio.inserir(produto_mapeado)
    return {"MSG": produto_inserido.id_produto}

@router.put("/api/editar_produto")
async def get_editar_produto(produto: EditarProdutoDTO = Body()):
    produto_mapeado = Mapper.MapperProduto.mapear_editar_produto_dto(produto)
    ProdutoRepositorio.alterar(produto_mapeado)
    return {"MSG": True}

@router.delete("/api/remover_produto")
async def get_remover_produto(id_produto: int):
    ProdutoRepositorio.remover(id_produto)
    return {"MSG": True}