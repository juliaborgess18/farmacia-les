from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dto.devolucao.cadastrar_devolucao_dto import CadastrarDevolucaoDTO
from infrastructure.repositories.devolucao import DevolucaoRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.devolucao import Devolucao
from schemas.produto import Produto
from util.mapper import Mapper

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
async def get_remover_devolucao(request: Request):
    devolucoes = DevolucaoRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/devolucao/visualizar_devolucao.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "devolucoes": devolucoes})

@router.post("/api/cadastrar_devolucao")
async def post_devolucao(devolucao: CadastrarDevolucaoDTO = Body()):

    devolucao_mapeada = Mapper.MapperDevolucao.mapear_cadastrar_devolucao_dto(devolucao)
    devolucao_inserida = DevolucaoRepositorio.inserir(devolucao_mapeada)

    for item in devolucao.itens_devolucao:
        VendaRepositorio.remover_item_venda(item.id_produto, devolucao.id_venda)

    return {"MSG": devolucao_inserida.id_devolucao}

@router.delete("/api/remover_devolucao")
async def delete_devolucao(id_devolucao: int):
    DevolucaoRepositorio.remover(id_devolucao)
    return {"MSG": True}
