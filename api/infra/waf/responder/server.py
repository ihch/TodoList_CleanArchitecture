import responder
import interface.controller.todo as controller
# import infra.database.sqlite3.sqlite3 as sqlite3
from infra.waf.responder.todo import GetTodo

import usecase.port.server.todo as response


class Server(GetTodo):
    def __init__(self):
        self.app = responder.API()

    def index(self, req, resp):
        resp.media = {"hoge": "poyo"}
        resp.status_code = 200

    def po(self, req, resp):
        _res = controller.TodoController().download_todos()
        # __res, http_status = response.DownloadTodosResponse(_res.todos)
        __res = response.DownloadTodosResponse(_res.todos).to_dict()
        http_status = 200
        # __res , http_status = [], 200
        resp.media = __res
        resp.status_code = http_status

    def set_router(self):
        self.app.add_route("/todo", self.get_todos)
        # self.app.add_route("/todo", self.po)
        self.app.add_route("/todo/{_id}", self.get_todo)
        self.app.add_route("/", self.index)

    def run(self):
        self.app.run()
