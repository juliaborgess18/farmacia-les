''' Arquivo principal para executar o programa'''

from model.dao.ConvenioDAO import ConvenioDAO
from model.dao.DevolucaoDAO import DevolucaoDAO
from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker
from model.domain.ItemDevolucao import ItemDevolucao
from model.dao.ProdutoDAO import ProdutoDAO
from model.dao.FormaPagamentoDAO import FormaPagamentoDAO
from model.dao.FornecedorDAO import FornecedorDAO
from model.dao.VendaDAO import VendaDAO
from model.dao.ItemVendaDAO import ItemVendaDAO

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
    
    
def print_itemVenda():
    print("========================")
    print("======== itemVenda =======")
    dao =  ItemVendaDAO ()
    ItemVenda = dao.select_all()

    for item in ItemVenda:
        print(f"qtd: {item.qtd}, idvenda: {item.idvenda}, idproduto: {item.idproduto}")
        
def main():
    print("Informação: Iniciando o Programa.")

    # print("Ainda não a nada aqui...")
    # printar_o_bom_garoto()
    print_itemVenda()
    print("Informação: Finalizando o Programa.")

if __name__ == "__main__":
    main()

