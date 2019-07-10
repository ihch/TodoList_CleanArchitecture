from typing import List
from domain.todo import Todo
from usecase.interactor.todo import TodoInteractor
from usecase.port.server.todo import DownloadTodoRequestParams
from interface.presenter.http import HTTPPresenter
from interface.gateway.database.rdb.todo import TodoRDBRepositoryAdapter


class TodoController:
    def __init__(self):
        self.input_port = TodoInteractor(
                HTTPPresenter(),
                TodoRDBRepositoryAdapter()
                )

    def download_todos(self) -> List[Todo]:
        res = self.input_port.download_todos()
        return res

    def download_todo(self, params: DownloadTodoRequestParams) -> Todo:
        return self.input_port.download_todo(params)
