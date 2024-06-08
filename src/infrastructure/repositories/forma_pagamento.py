from datetime import date
from typing import List, Optional

from sqlalchemy.exc import SQLAlchemyError
from infrastructure.config.database import get_db
from schemas.formaPagamento import FormaPagamento

class FormaPagamentoRepositorio:

    @classmethod
    def obter_todos(cls) -> Optional[List[FormaPagamento]]:
        try:
            db = get_db()
            return db.query(FormaPagamento).filter(FormaPagamento.foi_deletado == False).all()
        except SQLAlchemyError as ex:
            print(f"Error ao obter formas de pagamento: \n{ex}")
            return []