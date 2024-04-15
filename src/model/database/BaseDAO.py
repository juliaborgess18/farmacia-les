from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker

class BaseDAO():

    @classmethod
    def get_session(cls):
        engine = BaseORM.get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session