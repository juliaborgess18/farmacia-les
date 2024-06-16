from datetime import date
from typing import Optional
from pydantic import BaseModel
from dto.endereco.endereco import AlterarEnderecoDTO, CadastrarEnderecoDTO

class CadastrarClienteDTO(BaseModel):
    id_cliente: int = None
    nome: str 
    sobrenome: str 
    cpf: str 
    data_nascimento: str 
    tel_contato: str 
    endereco: CadastrarEnderecoDTO 
    
class AlterarClienteDTO(BaseModel):
    id_cliente: Optional[int] = None
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    data_nascimento: Optional[date] = None
    tel_contato: Optional[str] = None
    data_cadastro: Optional[date] = None
    cpf: Optional[str] = None
    endereco: Optional[AlterarEnderecoDTO] = None
    
    
    