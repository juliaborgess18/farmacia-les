from typing import Optional
from pydantic import BaseModel

class AlterarEnderecoDTO(BaseModel):
    rua: Optional[str] = None 
    numero: Optional[int] = None 
    bairro: Optional[str] = None 
    cidade: Optional[str] = None 
    uf: Optional[str] = None