from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dto.funcionario.funcionario import AlterarFuncionarioDTO, CadastrarFuncionarioDTO
from infrastructure.repositories.funcionario import FuncionarioRepositorio
from util.Mappers.funcionario.mapper_funcionario import MapperFuncionario

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Funcionário"
URL_ITEM = "funcionario"

@router.get("/funcionario", response_class=HTMLResponse)
async def get_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_funcionario", response_class=HTMLResponse)
async def get_cadastrar_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/cadastrar_funcionario.html", 
        {"request":request, 
         "funcItem": "Cadastrar", 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM
        }
    )
    
@router.post("/api/cadastrar_funcionario")
async def post_cadastrar_funcionario(funcionario:CadastrarFuncionarioDTO = Body()):
    funcionario_para_cadastrar = MapperFuncionario.cadastrar_funcionario(funcionario)
    FuncionarioRepositorio.inserir(funcionario_para_cadastrar)
    return {"MSG": True}

@router.get("/editar_funcionario", response_class=HTMLResponse)
async def get_editar_funcionario(request: Request, id_funcionario: int = 0):
    funcionario = FuncionarioRepositorio.obter_por_id(id_funcionario)
    return templates.TemplateResponse("/pages/funcionario/editar_funcionario.html", 
        {"request":request, 
        "funcItem": "Editar", 
        "navItem": NAV_ITEM, 
        "urlItem": URL_ITEM, 
        "funcionario":funcionario
        })

@router.put("/api/editar_funcionario")
async def put_editar_funcionario(funcionario: AlterarFuncionarioDTO):
    funcionario_para_alterar = MapperFuncionario.alterar_funcionario(funcionario)
    FuncionarioRepositorio.alterar(funcionario_para_alterar)
    return {"MSG":True}

@router.get("/remover_funcionario", response_class=HTMLResponse)
async def get_remover_funcionario(request: Request, id_funcionario : int = 0):
    funcionario = FuncionarioRepositorio.obter_por_id(id_funcionario)
    return templates.TemplateResponse("/pages/funcionario/remover_funcionario.html", 
        {"request":request, 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM, 
         "funcionario":funcionario
        })

@router.delete("/api/remover_funcionario")
async def delete_remover_funcionario(id_funcionario:int = 0):
    FuncionarioRepositorio.remover(id_funcionario)
    return {"MSG":True}
    

@router.get("/visualizar_funcionario", response_class=HTMLResponse)
async def get_visualizar_funcionario(request: Request):
    return templates.TemplateResponse("/pages/funcionario/visualizar_funcionario.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })