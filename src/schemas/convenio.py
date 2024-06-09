from datetime import date
from typing import Optional
from pydantic import BaseModel

class Convenio(BaseModel):
    id_convenio: Optional[int] = None
    especialidade: str
    cnpj: str
    id_cliente: int
