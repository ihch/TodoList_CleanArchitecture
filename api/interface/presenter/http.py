from typing import List
from domain.todo import Todo
from usecase.port.server.todo import (
    TodoOutputPort,
    DownloadTodoResponse,
    DownloadTodosResponse,
)


class HTTPPresenter(TodoOutputPort):
    def download_todos(self, todos: List[Todo]) -> DownloadTodosResponse:
        return DownloadTodosResponse(todos)

    def download_todo(self, todo: Todo) -> DownloadTodoResponse:
        return DownloadTodoResponse(todo)
