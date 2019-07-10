from abc import ABC, abstractmethod
from typing import List
from domain.todo import Todo


class TodoRepository(ABC):
    @abstractmethod
    def find_all(self) -> List[Todo]:
        pass

    @abstractmethod
    def find(self, _id: int) -> Todo:
        pass
