from abc import ABC, abstractmethod
from typing import Any

class Database(ABC):
    @abstractmethod
    def conectar(self) -> Any:
        pass

    @abstractmethod
    def desconectar(self, conn: Any) -> None:
        pass
