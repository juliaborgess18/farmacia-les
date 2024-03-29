from model.database.DatabasePostgreSQL import DatabasePostgreSQL

class DatabaseFactory:
    @staticmethod
    def get_database(nome):
        if nome == "postgresql":
            return DatabasePostgreSQL()
        return None
