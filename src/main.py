''' Arquivo principal para executar o programa'''

from model.dao.ClienteORM import ClienteORM
from model.database.DatabasePostgreSQL import DatabasePostgreSQL as db

if __name__ == "__main__":
    
    cliente_orm = ClienteORM()
    
    var = cliente_orm.selecionar_clientes()
    
    print(var)
    