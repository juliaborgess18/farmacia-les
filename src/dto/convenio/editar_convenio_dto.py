from pydantic import BaseModel


class EditarConvenioDTO(BaseModel):
    id_convenio: str
    especialidade: str
    cnpj: str