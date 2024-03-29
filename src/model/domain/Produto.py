import datetime

class Produto:
    def __init__(self, id_produto, nome, valor, data_validade: datetime):
        self.id_produto = id_produto
        self.nome = nome
        self.valor = valor
        self.data_validade = data_validade