from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.fornecedor import Fornecedor
from schemas.fornecedor import Fornecedor as FornecedorSchema
from util.mapper import Mapper


class FornecedorRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Fornecedor]]:
        try:
            db = get_db()
            return db.query(Fornecedor).filter(Fornecedor.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Fornecedor]:
        try:
            db = get_db()
            return db.query(Fornecedor).filter_by(id_fornecedor=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return Fornecedor()

    @classmethod
    def inserir(cls, fornecedor: FornecedorSchema) -> Optional[Fornecedor]:
        fornecedor_db = Mapper.mapear_fornecedor(fornecedor)
        try:
            db = get_db()
            db.add(fornecedor_db)
            db.commit()
            db.refresh(fornecedor_db)
            return fornecedor_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o fornecedor: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, fornecedor: FornecedorSchema):
        try:
            db = get_db()
            update_stmt = update(Fornecedor).where(Fornecedor.id_fornecedor == fornecedor.id_fornecedor).values(nome=fornecedor.nome,
                                                                                                                cnpj=fornecedor.cnpj,
                                                                                                                email=fornecedor.email,
                                                                                                                telefone=fornecedor.telefone,
                                                                                                                id_endereco=fornecedor.id_endereco)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o fornecedor: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Fornecedor).where(Fornecedor.id_fornecedor == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o fornecedor: \n{ex}")
            db.rollback()



