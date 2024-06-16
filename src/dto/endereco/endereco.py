from typing import Optional
from pydantic import BaseModel

class CadastrarEnderecoDTO(BaseModel):
    rua: str = None 
    numero: int = None 
    bairro: str = None 
    cidade: str = None 
    uf: str = None
    
class AlterarEnderecoDTO(BaseModel):
    rua: Optional[str] = None 
    numero: Optional[int] = None 
    bairro: Optional[str] = None 
    cidade: Optional[str] = None 
    uf: Optional[str] = None
    