from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter, Body, Query, Request
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
async def get_visualizar_funcionario(request: Request,
                                nome: Optional[str] = Query("", alias="nome"),
                                data_inicio: Optional[str] = Query(None, alias="data_inicio"),
                                data_final: Optional[str] = Query(None, alias="data_final"),
                                salario_min: Optional[str] = Query(None, alias="salario_min"),
                                salario_max: Optional[str] = Query(None, alias="salario_max")):
    
    data_admissao_inicial = datetime.strptime(data_inicio, "%Y-%m-%d").date() if not (data_inicio == None or data_inicio == '') else date.min
    data_admissao_final = datetime.strptime(data_final, "%Y-%m-%d").date() if not (data_final == None or data_final == '') else date.max

    valor_min = float(salario_min) if salario_min else 0
    valor_max = float(salario_max) if salario_max else float('inf')
    
    funcionarios = FuncionarioRepositorio.obter_com_filtros(nome,data_admissao_inicial, data_admissao_final, valor_min, valor_max)
    
    print(funcionarios)
    
    return templates.TemplateResponse("/pages/funcionario/visualizar_funcionario.html", 
        {"request":request, 
         "navItem": NAV_ITEM, 
         "urlItem": URL_ITEM,
         "nome":nome,
        "data_inicio": data_admissao_inicial,
        "data_final": data_admissao_final,
        "salario_min": valor_min,
        "salario_max": valor_max, 
        "funcionarios":funcionarios,
        }
    )