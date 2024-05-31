from datetime import date
from typing import List, Optional
from pydantic import BaseModel

from schemas.itemVenda import ItemVenda

class Venda(BaseModel):
    id_venda: Optional[int] = None
    data_venda: date
    valor_total: float
    status: str
    id_funcionario: int
    id_cliente: int
    id_formapagamento: int
    itens_venda: Optional[List[ItemVenda]] = None
