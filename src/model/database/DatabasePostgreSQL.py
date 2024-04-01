from sqlalchemy import create_engine

class DatabasePostgreSQL:

    # Replace with actual values
    username = 'farmacia-les'
    password = 'farmacia-les'
    hostname = '127.0.0.1:5432'
    database_name = 'farmacia-les'
    
    # Create the database engine
    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}/{database_name}')
    def abrir_conexao(self):
        with self.engine.connect() as conn:
            print("Conexão bem-sucedida")

    def fechar_conexao(self):
        with self.engine.connect() as conn:
            conn.close()
            print("Conexão fechada")