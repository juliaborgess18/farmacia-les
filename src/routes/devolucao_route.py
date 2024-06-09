from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from infrastructure.repositories.devolucao import DevolucaoRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.devolucao import Devolucao
from schemas.produto import Produto

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

@router.post("/cadastrar_devolucao")
async def get_cadastro_devolucao(devolucao: Devolucao = Body()):
    devolucao = DevolucaoRepositorio.inserir(devolucao)
    for item in devolucao.itens_devolucao:
        VendaRepositorio.remover_item_venda(item.id_produto, devolucao.id_venda)
    return {"MSG": devolucao.id_devolucao}