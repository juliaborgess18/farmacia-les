from typing import Optional
from pydantic import BaseModel, EmailStr
from dto.endereco.endereco import AlterarEnderecoDTO, CadastrarEnderecoDTO

class CadastrarFornecedorDTO(BaseModel):
    nome: str
    cnpj: str
    email: str
    telefone: str
    endereco: CadastrarEnderecoDTO

# class AlterarFornecedorDTO(BaseModel)
#     id_fornecedor: Optional[int]
#     nome: Optional[str]
#     cnpj: Optional[str]
#     email: Optional[EmailStr]
#     telefone: Optional[str]
#     endereco: Optional[AlterarEnderecoDTO]
