# import responder
# from domain.todo import Todo
from interface.controller.todo import TodoController
# import infra.waf.responder.request.todo as request
# import infra.waf.responder.response.todo as response
import usecase.port.server.todo as response


class GetTodo:
    def get_todos(self, req, resp):
        # _res = self.controller.download_todos()
        _res = TodoController().download_todos()
        __res = response.DownloadTodosResponse(_res.todos).to_dict()
        http_status = 200
        # __res, http_status = response.DownloadTodosResponse(_res)
        # resp.media = {"todos": __res}
        resp.media = __res
        resp.status_code = http_status

    async def get_todo(self, req, resp, *, _id):
        if type(_id) is not int:
            resp.status_code = 400
            return

        # _req = port.DownloadTodoRequestParams(_id)
        # _res = self.controller.download_todo(_req)
        _res, http_status = self.controller.download_todo(_id)
        resp.media = {"todo": _res}
        resp.status_code = http_status
