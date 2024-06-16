from pydantic import BaseModel


class EditarProdutoDTO(BaseModel):
    id_produto: str
    nome: str
    valor: str
    data_validade: str