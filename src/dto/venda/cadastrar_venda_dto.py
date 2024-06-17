from typing import List, Optional
from pydantic import BaseModel
from datetime import date

from infrastructure.repositories.produto import ProdutoRepositorio


class CadastrarItemVendaDTO(BaseModel):
    qtde: str
    id_produto: str
    
class CadastrarVendaDTO(BaseModel):
    id_forma_pagamento: str
    id_funcionario: str
    id_cliente: str
    itens_venda: List[CadastrarItemVendaDTO]