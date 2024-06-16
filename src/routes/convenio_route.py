from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter, Body, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dto.convenio.cadastrar_convenio_dto import CadastrarConvenioDTO
from dto.convenio.editar_convenio_dto import EditarConvenioDTO
from infrastructure.repositories.cliente import ClienteRepositorio
from infrastructure.repositories.convenio import ConvenioRepositorio
from util.mapper_convenio import MapperConvenio

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Convênio"
URL_ITEM = "convenio"

@router.get("/convenio", response_class=HTMLResponse)
async def get_convenio(request: Request):
    return templates.TemplateResponse("/pages/convenio/convenio.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_convenio", response_class=HTMLResponse)
async def get_cadastrar_convenio(request: Request):
    clientes = ClienteRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/convenio/cadastrar_convenio.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "clientes": clientes})

@router.get("/editar_convenio", response_class=HTMLResponse)
async def get_editar_convenio(request: Request, id_convenio: int = 0):
    convenio = ConvenioRepositorio.obter_por_id(id_convenio) if id_convenio is not 0 else None
    return templates.TemplateResponse("/pages/convenio/editar_convenio.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "convenio": convenio})

@router.get("/remover_convenio", response_class=HTMLResponse)
async def get_remover_convenio(request: Request, id_convenio: int = 0):
    convenio = ConvenioRepositorio.obter_por_id(id_convenio) if id_convenio is not 0 else None
    return templates.TemplateResponse("/pages/convenio/remover_convenio.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "convenio": convenio})

@router.get("/visualizar_convenio", response_class=HTMLResponse)
async def get_visualizar_convenio(  request: Request, 
                                    especialidade: Optional[str] = Query("", alias="especialidade"),
                                    data_inicio: Optional[str] = Query(None, alias="data_inicio"),
                                    data_final: Optional[str] = Query(None, alias="data_final")):
    
    parse_data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date() if not (data_inicio == None or data_inicio == '') else date.min
    parse_data_final = datetime.strptime(data_final, "%Y-%m-%d").date() if not (data_final == None or data_final == '') else date.max

    convenios = ConvenioRepositorio.obter_com_filtros(especialidade, parse_data_inicio, parse_data_final)
    return templates.TemplateResponse("/pages/convenio/visualizar_convenio.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "convenios": convenios})

@router.post("/api/cadastrar_convenio")
async def post_convenio(convenio: CadastrarConvenioDTO = Body()):
    convenio_mapeado = MapperConvenio.mapear_cadastrar_convenio_dto(convenio)
    convenio_inserido = ConvenioRepositorio.inserir(convenio_mapeado)
    return {"MSG": convenio_inserido.id_convenio}

@router.put("/api/editar_convenio")
async def put_convenio(convenio: EditarConvenioDTO = Body()):
    convenio_mapeado = MapperConvenio.mapear_editar_convenio_dto(convenio)
    ConvenioRepositorio.alterar(convenio_mapeado)
    return {"MSG": True}

@router.delete("/api/remover_convenio")
async def delete_convenio(id_convenio = int):
    print(f'entrou no método delete_convenio: {id_convenio}')
    ConvenioRepositorio.remover(id_convenio)
    return {"MSG": True}