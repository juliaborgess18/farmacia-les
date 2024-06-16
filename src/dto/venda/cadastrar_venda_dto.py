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

    # def calcular_valor_total(self):
    #     total = 0.0
    #     for item in self.itensVenda:
    #         # Buscar o valor unitário do produto com base no idProduto
    #         valor_unitario = self.buscar_valor_unitario_do_produto(item.idProduto)
    #         if valor_unitario is not None:
    #             total += item.qtde * valor_unitario
    #     self.valorTotal = total

    # def buscar_valor_unitario_do_produto(self, id_produto: int) -> Optional[float]:
    #     # Chame a função do seu repositório para buscar o valor unitário do produto
    #     produto = ProdutoRepositorio.obter_por_id(id_produto)
    #     if produto is not None:
    #         return produto.valor
    #     else:
    #         return None
