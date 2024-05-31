from datetime import date
from typing import List, Optional

import psycopg2
from sqlalchemy import update
from infrastructure.config.database import get_db
from infrastructure.models.funcionario import Funcionario
from schemas.funcionario import Funcionario as FuncionarioSchema
from util.mapper import Mapper

class FuncionarioRepositorio():

    @classmethod
    def obter_todos(cls) -> Optional[List[Funcionario]]:
        try:
            db = get_db()
            return db.query(Funcionario).filter(Funcionario.foi_deletado == False).all()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")     
            return []

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Funcionario]:
        try:
            db = get_db()
            return db.query(Funcionario).filter_by(id_funcionario=id).first()
        except psycopg2.Error as ex:
            print(f"Error ao buscar no banco: \n{ex}")     
            return Funcionario()

    @classmethod
    def inserir(cls, funcionario: FuncionarioSchema) -> Optional[Funcionario]:
        funcionario_db = Mapper.mapear_funcionario(funcionario)
        try:
            db = get_db()
            db.add(funcionario_db)
            db.commit()
            db.refresh(funcionario_db)
            return funcionario_db
        except psycopg2.Error as ex:
            print(f"Error ao inserir o funcionario: \n{ex}")
            db.rollback()

    @classmethod
    def alterar(cls, funcionario: FuncionarioSchema):
        try:
            db = get_db()
            update_stmt = update(Funcionario).where(Funcionario.id_funcionario == funcionario.id_funcionario).values(nome=funcionario.nome,
                                                                                                                     sobrenome=funcionario.sobrenome,
                                                                                                                     data_nascimento=funcionario.data_nascimento,
                                                                                                                     tel_contato=funcionario.tel_contato,
                                                                                                                     data_admissao=funcionario.data_admissao,
                                                                                                                     cargo=funcionario.cargo,
                                                                                                                     esta_ativo=funcionario.esta_ativo,
                                                                                                                     salario=funcionario.salario,
                                                                                                                     cpf=funcionario.cpf,
                                                                                                                     id_endereco=funcionario.id_endereco)
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao alterar o funcionario: \n{ex}")
            db.rollback()
   
    @classmethod
    def remover(cls, id: int):
        try:
            db = get_db()
            update_stmt = update(Funcionario).where(Funcionario.id_funcionario == id).values(foi_deletado=True, data_delete=date.today())
            db.execute(update_stmt)
            db.commit()
        except psycopg2.Error as ex:
            print(f"Error ao deletar o funcionario: \n{ex}")
            db.rollback()



