from sqlalchemy.orm import Session
from infrastructure.config.database import get_db
from infrastructure.models.formaPagamento import FormaPagamento

class FormaPagamentoRepositorio:
    @staticmethod
    def obter_todos():
        db_session = get_db()
        try:
            with db_session() as session:
                formas_pagamento = session.query(FormaPagamento).all()
                print("Formas de Pagamento encontradas:", formas_pagamento)
                return formas_pagamento
        finally:
            db_session.close()
