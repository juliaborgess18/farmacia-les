from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id_usuario: Optional[int] = None
    nome_usuario: str
    senha_usuario: str