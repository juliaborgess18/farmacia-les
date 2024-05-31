from typing import Optional

from pydantic import BaseModel

class Endereco(BaseModel):
    id_endereco: Optional[int] = None
    rua: str
    numero: int
    bairro: str
    cidade: str
    uf: str