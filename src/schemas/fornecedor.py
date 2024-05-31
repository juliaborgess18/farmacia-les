from typing import Optional
from pydantic import BaseModel

from schemas.endereco import Endereco

class Fornecedor(BaseModel):
    id_fornecedor: Optional[int] = None
    nome: str
    cnpj: str
    email: str
    telefone: str
    id_endereco: Optional[int] = None
    endereco: Optional[Endereco] = None
