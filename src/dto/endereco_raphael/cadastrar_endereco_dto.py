from pydantic import BaseModel

class EnderecoDTO(BaseModel):
    numero: int
    rua: str
    bairro: str
    cidade: str
    uf: str  # Sem validação de comprimento