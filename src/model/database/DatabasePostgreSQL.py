import psycopg2
import logging
from configparser import ConfigParser

class DatabasePostgreSQL:
    def __init__(self):
        self.connection = None
        self.url = ""
        self.login = ""
        self.senha = ""

    def conectar(self):
        try:
            self.carregar_propriedades()
        except Exception as ex:
            logging.getLogger(__name__).exception("Erro ao carregar propriedades", exc_info=ex)
            return None

        try:
            self.connection = psycopg2.connect(database=self.url, user=self.login, password=self.senha)
            return self.connection
        except psycopg2.Error as ex:
            logging.getLogger(__name__).exception("Erro ao conectar ao PostgreSQL", exc_info=ex)
            return None

    def desconectar(self, connection):
        try:
            connection.close()
        except psycopg2.Error as ex:
            logging.getLogger(__name__).exception("Erro ao desconectar do PostgreSQL", exc_info=ex)

    def carregar_propriedades(self):
        parser = ConfigParser()
        parser.read("src/maissaudeplus/propriedades/conf.properties")

        self.url = parser.get("db.postgres", "url")
        self.login = parser.get("db.postgres", "login")
        self.senha = parser.get("db.postgres", "password")