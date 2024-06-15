from typing import Optional
from fastapi import APIRouter, Body, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dto.devolucao.cadastrar_devolucao_dto import CadastrarDevolucaoDTO
from dto.devolucao.editar_devolucao_dto import EditarDevolucaoDTO
from infrastructure.repositories.devolucao import DevolucaoRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.devolucao import Devolucao
from schemas.produto import Produto
from util.mapper import Mapper
from util.mapper_devolucao import MapperDevolucao

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Devolução"
URL_ITEM = "devolucao"

@router.get("/devolucao", response_class=HTMLResponse)
async def get_devolucao(request: Request):
    return templates.TemplateResponse("/pages/devolucao/devolucao.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_devolucao", response_class=HTMLResponse)
async def get_cadastro_devolucao(request: Request, id_venda: int = 0):
    venda = VendaRepositorio.obter_por_id(id_venda)
    return templates.TemplateResponse("/pages/devolucao/cadastrar_devolucao.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "venda": venda})

@router.get("/editar_devolucao", response_class=HTMLResponse)
async def get_editar_devolucao(request: Request, id_devolucao: int = 0):
    devolucao = DevolucaoRepositorio.obter_por_id(id_devolucao) if id_devolucao != 0 else None
    venda = VendaRepositorio.obter_por_id(id_devolucao) if devolucao != 0 else None
    return templates.TemplateResponse("/pages/devolucao/editar_devolucao.html", 
    {
        "request":request, 
        "navItem": NAV_ITEM, 
        "urlItem": URL_ITEM, 
        "devolucao": devolucao,
        "venda": venda 
    })

@router.get("/remover_devolucao", response_class=HTMLResponse)
async def get_remover_devolucao(request: Request, id_devolucao: int = 0):
    devolucao = DevolucaoRepositorio.obter_por_id(id_devolucao) if id_devolucao != 0 else None
    return templates.TemplateResponse("/pages/devolucao/remover_devolucao.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "devolucao": devolucao})

@router.get("/visualizar_devolucao", response_class=HTMLResponse)
async def get_visualizar_devolucao(     request: Request, 
                                        id_venda: Optional[str] = Query(None, alias="id_venda"),
                                        valor_min: Optional[str] = Query(None, alias="valor_min"),
                                        valor_max: Optional[str] = Query(None, alias="valor_max")):
    
    print("get_visualizar_devolucao")
    print(id_venda)
    parse_id_venda = id_venda if id_venda != '' else None
    parse_valor_min = float(valor_min) if not (valor_min == None or valor_min == '') else 0
    parse_valor_max = float(valor_max) if not (valor_max == None or valor_max == '') else float('inf')

    devolucoes = DevolucaoRepositorio.obter_com_filtros(parse_id_venda, parse_valor_min, parse_valor_max)

    return templates.TemplateResponse("/pages/devolucao/visualizar_devolucao.html", 
    {
        "request":request, 
        "navItem": NAV_ITEM, 
        "urlItem": URL_ITEM, 
        "devolucoes": devolucoes
    })

@router.post("/api/cadastrar_devolucao")
async def post_devolucao(devolucao: CadastrarDevolucaoDTO = Body()):

    devolucao_mapeada = MapperDevolucao.mapear_cadastrar_devolucao_dto(devolucao)
    devolucao_inserida = DevolucaoRepositorio.inserir(devolucao_mapeada)

    for item in devolucao.itens_devolucao:
        VendaRepositorio.remover_item_venda(item.id_produto, devolucao.id_venda)

    return {"MSG": devolucao_inserida.id_devolucao}

@router.put("/api/editar_devolucao")
async def put_devolucao(devolucao: EditarDevolucaoDTO = Body()):
    devolucao_mapeada = MapperDevolucao.mapear_editar_devolucao_dto(devolucao)
    DevolucaoRepositorio.alterar_item_devolucao(devolucao_mapeada)
    return {"MSG": True}

@router.delete("/api/remover_devolucao")
async def delete_devolucao(id_devolucao: int):
    DevolucaoRepositorio.remover(id_devolucao)
    return {"MSG": True}
