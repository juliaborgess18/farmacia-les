from pydantic import BaseModel

class EditarDevolucaoDTO(BaseModel):
    id_produto: str
    id_devolucao: str
    qtde: str