from model.domain.Cliente import Cliente
from model.domain.Devolucao import Devolucao
from model.domain.Endereco import Endereco
from model.domain.FormaPagamento import FormaPagamento
from model.domain.Fornecedor import Fornecedor
from model.domain.Funcionario import Funcionario
from model.domain.ItemDevolucao import ItemDevolucao
from model.domain.ItemVenda import ItemVenda
from model.domain.Medico import Medico
from model.domain.Produto import Produto
from model.domain.Venda import Venda

def main():
    
    endereco = Endereco("cidade", "estado", "uf", "bairro", "rua-12345", 1)
    data_nascimento = "18/05/2000"
    tel_contato = "28999251155"
    nome = "Python"
    sobrenome = "3.9"
    id_cliente = 1
    data_cadastro = "11/03/2024"
    cpf = "185.259.748-88"
    
    cliente = Cliente(endereco, data_nascimento, tel_contato, nome, sobrenome, id_cliente, data_cadastro, cpf)
    print("Cliente: " + cliente.nome + ' ' + cliente.sobrenome) 

    medico = Medico(endereco, data_nascimento, tel_contato, nome, sobrenome, id_cliente)
    print("Médico: " + medico.nome + ' ' + medico.sobrenome) 

    funcionario = Funcionario(endereco, data_nascimento, tel_contato, nome, sobrenome, id_cliente)
    print("Funcionário: " + funcionario.nome + ' ' + funcionario.sobrenome) 

    item_devolucao_1 = ItemDevolucao(1, 1, 5)
    item_devolucao_2 = ItemDevolucao(1, 2, 7)
    item_devolucao_3 = ItemDevolucao(1, 3, 9)
    itens_devolucao = []
    itens_devolucao.append(item_devolucao_1)
    itens_devolucao.append(item_devolucao_2)
    itens_devolucao.append(item_devolucao_3)

    devolucao = Devolucao(1, 500.0, 1, itens_devolucao)
    print(f"Devolucao: {devolucao.valor_devolucao}")
    for item in devolucao.itens_devolucao:
        print(f"Item id_devolução: {item.id_devolucao}, id_produto: {item.id_produto} e qtd: {item.qtd}")

    forma_pagamento = FormaPagamento(1, "Pix")
    print(f"Forma de Pagamento: {forma_pagamento.nome}")

    item_venda_1 = ItemVenda(1, 1, 2)
    item_venda_2 = ItemVenda(1, 2, 3)
    item_venda_3 = ItemVenda(1, 3, 4)
    itens_venda = []
    itens_venda.append(item_venda_1)
    itens_venda.append(item_venda_2)
    itens_venda.append(item_venda_3)

    venda = Venda(1, '2024-03-29', 1, 1, 123.0, 'Completa', itens_venda)

    print(f"Venda: {venda.valor_total}")
    for item in venda.itens_venda:
        print(f"Item id_devolução: {item.id_venda}, id_produto: {item.id_produto} e qtd: {item.qtd}")

    fornecedor = Fornecedor('23.135.161/0001-00', 'teste@email.com', '(28)99988-7766', 'Forncedor-1')
    print(f"Fornecedor: {fornecedor.nome}")

    produto = Produto(1, 'produto-1', 25.0, '2024-12-31')
    print(f"Produto: {produto.nome}")


if __name__ == "__main__":
    main()