''' Arquivo principal para executar o programa'''
import sys
from model.dao.ConvenioDAO import ConvenioDAO
from model.dao.DevolucaoDAO import DevolucaoDAO
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.ItemDevolucao import ItemDevolucao
from model.dao.ProdutoDAO import ProdutoDAO

def printar_o_bom_garoto():
    print('''
         .--.             .---.
        /:.  '.         .' ..  '._.---.
       /:::-.  \.-"""-;` .-:::.     .::\\
      /::'|  `\/  _ _  \\'   `\:'   ::::|
  __.'    |   /  (o|o)  \     `'.   ':/
 /    .:. /   |   ___   |        '---'
|    ::::'   /:  (._.) .:\\
\    .='    |:'        :::|
 `""`       \     .-.   ':/
             '---`|I|`---'
                  '-'        

          ''')
    
    print("au au...")

def main():
    print("Informação: Iniciando o Programa.")

    print("Ainda não a nada aqui...")
    printar_o_bom_garoto()
     
    print("Informação: Finalizando o Programa.")

if __name__ == "__main__":
    main()
    # clienteDAO.delete(clienteDAO.select_by_id(2))
    # clienteDAO = ClienteDAO()
    # result = clienteDAO.select_by_id(2)
    # result.nome = 'Systech'
    # clienteDAO.update(result)
    # print(result.nome)

