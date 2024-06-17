from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import text, update
from dto.relatorios.relatorio_quantidade_produtos_vendidos import RelatorioQuantidadeProdutosVendidosDTO
from infrastructure.config.database import get_db
from infrastructure.models.itemVenda import ItemVenda
from infrastructure.models.venda import Venda
from schemas.venda import Venda as VendaSchema
from util.constantes import RELATORIO_QTDE_PRODUTOS_VENDIDOS
from util.mapper import Mapper

class VendaRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Venda]]:
        try:
            db = get_db()
            return db.query(Venda).filter(Venda.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscas a venda: \n{ex}")    
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Venda]:
        try:
            db = get_db()
            return db.query(Venda).filter_by(id_venda=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscas a venda: \n{ex}")    
            return Venda()

    @classmethod
    def inserir(cls, venda: Venda) -> Optional[Venda]:
        try:
            db = get_db()
            db.add(venda)
            db.commit()
            db.refresh(venda)
            return venda
        except psycopg2.Error as ex:
            print(f"Error ao inserir o venda: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, venda: VendaSchema):
        try:
            db = get_db()
            update_stmt = update(Venda).where(Venda.id_venda == venda.id_venda).values(data_venda=venda.data_venda,
                                                                                       valor_total=venda.valor_total,
                                                                                       status=venda.status,
                                                                                       data_delete=None,
                                                                                       foi_deletado=False,
                                                                                       id_funcionario=venda.id_funcionario,
                                                                                       id_cliente=venda.id_cliente,
                                                                                       id_formapagamento=venda.id_formapagamento)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o cliente: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Venda).where(Venda.id_venda == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o venda: \n{ex}")
            db.rollback()

    @classmethod
    def obter_itens_venda_por_id_venda(cls, id: int):
        try:
            db = get_db()
            return db.query(ItemVenda).filter(ItemVenda.id_venda == id).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscas os itens de venda: \n{ex}")    
            return []


    @classmethod
    def remover_item_venda(cls, id_produto, id_venda):
        try:
            db = get_db()
            items_delete = db.query(ItemVenda).filter(
                ItemVenda.id_produto == id_produto,
                ItemVenda.id_venda == id_venda
            ).all()

            valor_retirado = 0
            for item in items_delete:
                valor_retirado += item.produto.valor*item.qtde
                db.delete(item)
            venda = db.query(Venda).filter_by(id_venda=id_venda).first()
            venda.valor_total -= valor_retirado

            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao buscas os itens de venda: \n{ex}")   
            db.rollback() 
            return []
        
    @classmethod
    def obter_quantidade_produtos_vendidos(cls, data_inicio: date, data_final: date) -> List:
        try:
            db = get_db()
            query = text(RELATORIO_QTDE_PRODUTOS_VENDIDOS)
            resultado = db.execute(query, {'data_inicio': data_inicio, 'data_final': data_final})
            return resultado
        except psycopg2.Error as ex:
            print(f"Error ao gerar o relatório: \n{ex}")    
            return []