''' Arquivo principal para executar o programa'''

from model.dao.ConvenioDAO import ConvenioDAO

def main():
    print("Informação: Iniciando o Programa.")
    dao = ConvenioDAO()

    convenios = dao.select_all()

    for convenio in convenios:
        print(f"Id: {convenio.idconvenio}, Especialidade: {convenio.especialidade}, Data do inicio do convênio: {convenio.data_inicio_convenio}, CNPJ: {convenio.cnpj}, Id do cliente: {convenio.idcliente}, Nome do Médico: {convenio.cliente.nome} {convenio.cliente.sobrenome}")
    
    print("Informação: Finalizando o Programa.")

if __name__ == "__main__":
    main()
