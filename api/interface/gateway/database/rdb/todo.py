from typing import List
from domain.todo import Todo
# from interface.gateway.database.rdb.handler import SqlHandler
from infra.database.sqlite3.sqlite3 import SqlHandler


class TodoRDBRepositoryAdapter(SqlHandler):
    def find_all(self) -> List[Todo]:
        todos: List[Todo] = []
        rows = self.query("SELECT id, name, description FROM todo")
        for row in rows:
            _id, name, description = tuple(row)
            todos.append(Todo(_id, name, description))
        return todos

    def find_by_id(self, __id: int) -> Todo:
        # Todo._idはユニークな値なので一意に定まる
        row = self.query(
                "SELECT id, name, description FROM todo WHERE id = ?",
                __id
                )
        if row.__len__():
            return None
        _id, name, description = tuple(row[0])
        return Todo(_id, name, description)
