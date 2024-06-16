from datetime import date
from typing import Optional
from pydantic import BaseModel
from dto.endereco.endereco import AlterarEnderecoDTO, CadastrarEnderecoDTO

class CadastrarFuncionarioDTO(BaseModel):
    nome: str 
    sobrenome: str 
    data_nascimento: str 
    tel_contato: str 
    data_admissao: str 
    cargo: str 
    salario: str 
    cpf: str 
    endereco: CadastrarEnderecoDTO 
    
class AlterarFuncionarioDTO(BaseModel):
    id_funcionario: Optional[int] 
    nome: Optional[str] 
    sobrenome: Optional[str] 
    data_nascimento: Optional[str] 
    tel_contato: Optional[str] 
    data_admissao: Optional[str] 
    cargo: Optional[str] 
    salario: Optional[str] 
    cpf: Optional[str] 
    endereco: Optional[AlterarEnderecoDTO]  