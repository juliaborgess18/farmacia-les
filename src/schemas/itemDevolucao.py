from typing import Optional
from pydantic import BaseModel

class ItemDevolucao(BaseModel):
    qtde: int
    id_produto: int
    id_devolucao: Optional[int] = None