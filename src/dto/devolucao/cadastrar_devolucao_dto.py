from typing import List

from pydantic import BaseModel

class ItemDevolucaoDTO(BaseModel):
    qtde: str
    id_produto: str

class CadastrarDevolucaoDTO(BaseModel):
    id_venda: str
    valor_devolucao: str
    itens_devolucao: List[ItemDevolucaoDTO]
