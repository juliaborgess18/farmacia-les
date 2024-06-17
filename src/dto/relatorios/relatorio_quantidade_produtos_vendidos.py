from pydantic import BaseModel


class RelatorioQuantidadeProdutosVendidosDTO(BaseModel):
    id_produto: str
    nome: str
    qtde: str
    valor_unitario: str
    valor_total: str