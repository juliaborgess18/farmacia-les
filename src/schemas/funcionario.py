from datetime import date
from typing import Optional
from pydantic import BaseModel

from schemas.endereco import Endereco

class Funcionario(BaseModel):
    id_funcionario: Optional[int] = None
    nome: str
    sobrenome: str
    data_nascimento: date
    tel_contato: str
    data_admissao: date
    cargo: str
    esta_ativo: bool
    salario: float
    cpf: str
    id_endereco: Optional[int] = None
    endereco: Optional[Endereco] = None
