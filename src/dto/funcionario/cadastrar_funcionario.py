from datetime import date
from typing import Optional
from pydantic import BaseModel
from dto.endereco.endereco import CadastrarEnderecoDTO

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