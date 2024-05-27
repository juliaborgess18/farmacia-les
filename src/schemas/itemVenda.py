from typing import Optional
from pydantic import BaseModel

class ItemVenda(BaseModel):
    qtde: int
    id_produto: int
    id_venda: Optional[int] = None
