from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from infrastructure.repositories.venda import VendaRepositorio
from util.mapper_relatorios import MapperRelatorios

router = APIRouter()

templates = Jinja2Templates(directory="templates")
URL_PREFIXO = "/relatorios"

@router.get(f"{URL_PREFIXO}/itens_mais_vendidos", response_class=HTMLResponse)
async def get_produto(request: Request, 
                      data_inicio: Optional[str] = Query(None, alias="data_inicio"),
                      data_final: Optional[str] = Query(None, alias="data_final"),):
    
    parse_data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date() if not (data_inicio == None or data_inicio == '') else date.min
    parse_data_final = datetime.strptime(data_final, "%Y-%m-%d").date() if not (data_final == None or data_final == '') else date.max

    relatorio = VendaRepositorio.obter_quantidade_produtos_vendidos(parse_data_inicio, parse_data_final)
    relatorio_mapeado = MapperRelatorios.mapear_relatorio_quantidade_produtos_vendidos(relatorio)

    return templates.TemplateResponse("/pages/relatorios/produtos_mais_vendidos.html", {"request":request, "itens_mais_vendidos": relatorio_mapeado })

