from pydantic import BaseModel


class CadastrarConvenioDTO(BaseModel):
    especialidade: str
    cnpj: str
    id_cliente: str