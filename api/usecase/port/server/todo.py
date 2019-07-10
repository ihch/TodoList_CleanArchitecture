from abc import ABC, abstractmethod
from typing import List, Dict
from domain.todo import Todo


class DownloadTodoResponse:
    def __init__(self, todo: Todo):
        self.todo = todo

    def to_dict(self) -> Dict:
        res = {
            "id": self.todo._id,
            "name": self.todo.name,
            "description": self.todo.description
            }
        return {"todo": res}


class DownloadTodosResponse:
    def __init__(self, todos: List[Todo]):
        self.todos = todos

    def to_dict(self) -> Dict:
        res = []
        for todo in self.todos:
            todo: Todo
            res.append({
                "id": todo._id,
                "name": todo.name,
                "description": todo.description
                })
        return {"todos": res}


class DownloadTodoRequestParams:
    def __init__(self, _id: int):
        self._id = _id


class TodoInputPort(ABC):
    @abstractmethod
    def download_todos(self) -> DownloadTodosResponse:
        pass

    @abstractmethod
    def download_todo(
            self,
            params: DownloadTodoRequestParams
            ) -> DownloadTodoResponse:
        pass


class TodoOutputPort(ABC):
    @abstractmethod
    def download_todos(self, todos: List[Todo]) -> DownloadTodosResponse:
        pass

    @abstractmethod
    def download_todo(self, todo: Todo) -> DownloadTodoResponse:
        pass
