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
    # main()
    clienteDAO = ClienteDAO()

    cliente_para_deletar = clienteDAO.select_by_id(1)
    clienteDAO.delete(cliente_para_deletar)
    result = clienteDAO.select_all()

    for item in result:
        print(f"Id: {item.id_cliente}, Nome: {item.nome}. ")

