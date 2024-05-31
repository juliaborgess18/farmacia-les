from datetime import date
from typing import Optional
from pydantic import BaseModel

class Convenio(BaseModel):
    id_convenio: Optional[int] = None
    especialidade: str
    data_inicio_convenio: date
    cnpj: str
    id_cliente: int
