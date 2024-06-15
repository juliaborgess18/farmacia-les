from pydantic import BaseModel

class CadastrarProdutoDTO(BaseModel):
    nome: str
    valor: str
    data_validade: str
    id_fornecedor: str