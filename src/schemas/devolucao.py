from typing import List, Optional
from pydantic import BaseModel

from schemas.itemDevolucao import ItemDevolucao

class Devolucao(BaseModel):
    id_devolucao: Optional[int] = None
    id_venda: int
    valor_devolucao: float
    itens_devolucao: Optional[List[ItemDevolucao]] = None
