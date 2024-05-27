from typing import Optional
from pydantic import BaseModel

class FormaPagamento(BaseModel):
    id_formapagamento: Optional[int] = None
    nome: str