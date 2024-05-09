import datetime
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

from model.dao.VendaDAO import VendaDAO
from model.database.BaseDAO import BaseDAO
from model.domain.Venda import Venda
from model.domain.ItemVenda import ItemVenda
from model.dao.ItemVendaDAO import ItemVendaDAO

class CadastroVendaController(QWidget):
    session = BaseDAO.get_session()
    vendaDAO = VendaDAO(session)
    itemVendaDAO = ItemVendaDAO(session)
    
    def __init__(self):
        super().__init__()
        loadUi('src/view/CadastroVendaView.ui', self)
        self.pushButton_venda.clicked.connect(self.inserir_venda)
        self.pushButton_item_venda.clicked.connect(self.inserir_item_venda)
        self.carrinho = []

    def inserir_item_venda(self):
        try:
            id_produto = int(self.input_id_produto.text())
            qtd = int(self.input_qtd_produto.text())

            #teste
            print(f"ID Produto: {id_produto}, Quantidade: {qtd}")

            item_venda = ItemVenda(qtd=qtd, id_produto=id_produto)
            #teste
            print(f"Item Venda: {item_venda}")
            self.carrinho.append(item_venda)

            item_text = f"Produto: {id_produto}, Quantidade: {qtd}"
            list_item = QListWidgetItem(item_text)
            self.listWidget_produto.addItem(list_item)
            #teste
            print(f"Carrinho atual: {self.carrinho}")
            # NAO FUNCIONOU
            self.atualizar_valor_pagamento()  # Atualiza o valor no frame_valor_pagamento
            
            QMessageBox.information(self, 'Alerta', 'Sucesso ao adicionar o item de venda.')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Alerta', f'Erro ao adicionar o item de venda.')

    def atualizar_valor_pagamento(self):
        total = 0
        for item in self.carrinho:
            if item.produto:  # Verifica se o produto está definido
                valor_item = item.qtd * item.produto.valor
                total += valor_item  # Calcula o total do carrinho
            else:
                print("Erro: Produto não definido para o ItemVenda")

        self.label_valor_pagamento.setText(f"Valor total: R${total:.2f}")  # Atualiza o texto do QLabel
        self.label_valor_pagamento.repaint()  # Atualiza o valor total na interface gráfica


    def inserir_venda(self):
        try:
            venda = Venda()
        
            venda.id_funcionario = self.input_id_funcionario.text()
            venda.id_cliente = self.input_id_cliente.text()
            venda.id_formapagamento = self.input_id_forma_pagamento.text()
            venda.data_venda = datetime.date.today()
            
            # Calcular o valor total da venda com base nos itens do carrinho
            total_venda = sum(item.qtd * item.produto.valor if item.produto else 0 for item in self.carrinho)
            venda.valor_total = total_venda
            
            venda.status = 'Concluída'

            venda.item_venda = self.carrinho  # Associa o carrinho à venda
            
            self.vendaDAO.insert(venda)
            
            QMessageBox.information(self, 'Alerta', 'Sucesso ao cadastrar a venda.')
        except Exception as e:
            print(e)
            QMessageBox.critical(self, 'Alerta', f'Erro ao cadastrar a venda.')
