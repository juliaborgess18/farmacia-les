import sqlite3

#from model.domain import Fornecedor

class FornecedorDAO:
    def __init__(self):
        self.connection = None