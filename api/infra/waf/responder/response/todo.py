from typing import List, Tuple
from domain.todo import Todo
from usecase.port.server.todo import DownloadTodoResponse, DownloadTodosResponse


class TodoResult:
    def __init__(self, todo: Todo):
        self.result = todo


class TodosResult:
    def __init__(self, todos: List[Todo]):
        self.results = todos


def todo_response_adapter(_res: DownloadTodoResponse) -> Tuple[TodoResult, int]:
    http_status = 200
    if _res.todo is None:
        http_status = 204
    res = TodoResult(_res.todo)
    return res, http_status


def todos_responder_adapter(
    _res: DownloadTodosResponse
) -> Tuple[TodosResult, int]:
    http_status = 200
    if _res.todos.__len__ == 0:
        http_status = 204
    res = TodosResult(_res.todos)
    return res, http_status
