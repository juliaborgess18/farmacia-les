from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy.orm import joinedload
from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.cliente import Cliente
from schemas.cliente import Cliente as ClienteSchema
from util.mapper import Mapper

class ClienteRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Cliente]]:
        try:
            db = get_db()
            return db.query(Cliente).filter(Cliente.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")    
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Cliente]:
        try:
            db = get_db()
            return db.query(Cliente).filter_by(id_cliente=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")       
            return Cliente()

    @classmethod
    def inserir(cls, cliente: ClienteSchema) -> Optional[Cliente]:
        cliente_db = Mapper.mapear_cliente(cliente)
        try:
            db = get_db()
            db.add(cliente_db)
            db.commit()
            db.refresh(cliente_db)
            return cliente_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o cliente: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, cliente: ClienteSchema):
        try:
            db = get_db()
            update_stmt = update(Cliente).where(Cliente.id_cliente == cliente.id_cliente).values(nome=cliente.nome,
                                                                                                sobrenome=cliente.sobrenome,
                                                                                                data_nascimento=cliente.data_nascimento,
                                                                                                tel_contato=cliente.tel_contato,
                                                                                                data_cadastro=cliente.data_cadastro,
                                                                                                cpf=cliente.cpf,
                                                                                                id_endereco=cliente.id_endereco)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o cliente: \n{ex}")
            db.rollback()

    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Cliente).where(Cliente.id_cliente == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o cliente: \n{ex}")
            db.rollback()
