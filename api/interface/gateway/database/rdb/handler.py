from abc import ABC, abstractmethod
from domain.todo import Todo


class Result(ABC):
    @abstractmethod
    def last_insert_id(self) -> int:
        pass


class SqlHandler(ABC):
    @abstractmethod
    def execute(self, sql: str, *args) -> Result:
        pass

    @abstractmethod
    def query(self, sql: str, *args) -> Todo:
        pass
