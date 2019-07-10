from usecase.port.server.todo import (
        TodoInputPort,
        DownloadTodosResponse,
        DownloadTodoResponse,
        DownloadTodoRequestParams
)
from interface.presenter.http import HTTPPresenter
from usecase.port.repository.todo import TodoRepository


class TodoInteractor(TodoInputPort):
    def __init__(
            self,
            output_port: HTTPPresenter,
            todo_repository: TodoRepository
            ):
        self.output_port = output_port
        self.todo_repository = todo_repository

    def download_todos(self) -> DownloadTodosResponse:
        res = self.todo_repository.find_all()
        if res is None:
            return self.output_port.download_todos([])
        return self.output_port.download_todos(res)

    def download_todo(
            self,
            params: DownloadTodoRequestParams
            ) -> DownloadTodoResponse:
        res = self.todo_repository.find(params._id)
        if res is None:
            return None
        return self.output_port.download_todo(res)
