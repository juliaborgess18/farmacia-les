from model.database.BaseORM import BaseORM
from sqlalchemy.orm import sessionmaker

class ClienteDAO():
    engine = ''
    session = ''

    def __init__(self):
        self.engine = BaseORM.get_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()