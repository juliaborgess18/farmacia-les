from fastapi import APIRouter, Body, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dto.venda.cadastrar_venda_dto import CadastrarVendaDTO
from infrastructure.repositories.fornecedor import FornecedorRepositorio
from infrastructure.repositories.venda import VendaRepositorio
from schemas.venda import Venda
from util.mapper_venda import MapperVenda

router = APIRouter()

templates = Jinja2Templates(directory="templates")
NAV_ITEM = "Venda"
URL_ITEM = "venda"

@router.get("/venda", response_class=HTMLResponse)
async def get_venda(request: Request):
    return templates.TemplateResponse("/pages/vendas/venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/cadastrar_venda", response_class=HTMLResponse)
async def get_cadastrar_venda(request: Request):
    fornecedores = FornecedorRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/cadastrar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "fornecedores": fornecedores })

@router.get("/editar_venda", response_class=HTMLResponse)
async def get_editar_venda(request: Request):
    return templates.TemplateResponse("/pages/vendas/editar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM })

@router.get("/remover_venda", response_class=HTMLResponse)
async def get_remover_venda(request: Request):
    vendas = VendaRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/remover_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "vendas": vendas })

@router.get("/visualizar_venda", response_class=HTMLResponse)
async def get_visualizar_venda(request: Request):
    vendas = VendaRepositorio.obter_todos()
    return templates.TemplateResponse("/pages/vendas/visualizar_venda.html", {"request":request, "navItem": NAV_ITEM, "urlItem": URL_ITEM, "vendas": vendas })

@router.post("/api/cadastrar_venda")
async def post_venda(venda: CadastrarVendaDTO = Body()):
    venda_mapeada = MapperVenda.mapear_venda(venda)
    item_venda_mapeada = MapperVenda.mapear_itens_venda(venda)
    venda_inserida = VendaRepositorio.inserir(venda_mapeada)
    
    # Lógica adicional aqui, se necessário
    
    return {"MSG": venda_inserida.id_venda}

# @router.post("/api/cadastrar_venda")
# async def post_venda(venda: CadastrarVendaDTO = Body()):
#     try:
#         # Adicionando logs para verificar os dados recebidos e o cálculo do valor total
#         print("Dados recebidos para cadastro da venda:")
#         print(venda.dict())

#         venda.calcular_valor_total()  # Calcula o valor total da venda
#         print("Valor total da venda calculado:", venda.valorTotal)

#         venda_mapeada = MapperVenda.mapear_venda(venda)
#         print("Venda mapeada para inserção no banco de dados:", venda_mapeada.dict())

#         venda_inserida = VendaRepositorio.inserir(venda_mapeada)
#         print("Venda inserida no banco de dados:", venda_inserida.dict())

#         return {"MSG": venda_inserida.id_venda}
#     except Exception as e:
#         # Log para capturar exceções
#         print(f"Erro ao cadastrar venda: {e}")
#         return {"error": str(e)}
