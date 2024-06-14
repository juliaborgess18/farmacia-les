from datetime import date
from typing import Optional
from pydantic import BaseModel
from schemas.endereco import Endereco

class Cliente(BaseModel):
    id_cliente: Optional[int] = None
    nome: str
    sobrenome: str
    data_nascimento: date
    tel_contato: str
    cpf: str
    id_endereco: Optional[int] = None
    endereco: Optional[Endereco] = None
    data_cadastro: Optional[date] = None

