from datetime import date
from typing import Optional
from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: Optional[int] = None
    nome: str
    valor: float
    data_validade: date
    id_fornecedor: int
