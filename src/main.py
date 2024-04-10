''' Arquivo principal para executar o programa'''

from model.dao.ProdutoDAO import ProdutoDAO

def main():
    print("Informação: Iniciando o programa")

    dao = ProdutoDAO()    
    produtos = dao.select_all()
    
    for produto in produtos:
        print(f"Id: {produto.idproduto}, Nome: {produto.nome}, Valor: {produto.valor}, Data: {produto.data_validade}")

    print("Informação: Encerrando o programa")

if __name__ == "__main__":
    main()

    

    