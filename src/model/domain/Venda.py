import datetime

class Venda:
    def __init__(self, id_venda, data_venda: datetime, id_comprador, id_vendedor, valor_total, status, itens_venda):
        self.id_venda = id_venda
        self.data_venda = data_venda
        self.id_comprador = id_comprador
        self.id_vendedor = id_vendedor
        self.valor_total = valor_total
        self.status = status
        self.itens_venda = itens_venda