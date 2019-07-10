import sqlite3
from typing import List
from domain.todo import Todo
from interface.gateway.database.rdb.handler import (
        SqlHandler as AbsSqlHandler,
        Result as AbsResult
        )


class Result(AbsResult):
    def __init__(self, result: sqlite3.Cursor):
        self.result = result

    def last_insert_id(self) -> int:
        return self.result.lastrowid


class SqlHandler(AbsSqlHandler):
    def __init__(self):
        self.connection = sqlite3.connect('develop.db')
        if self.connection is None:
            raise('db connecting error')

    def execute(self, sql: str, *args) -> Result:
        cur = self.connection.cursor()
        self.connection.commit()
        res = cur.execute(sql, args)
        if res is None:
            return None
        return Result(res)

    def query(self, sql: str, *args) -> List[Todo]:
        cur = self.connection.cursor()
        res = cur.execute(sql, args)
        if res is None:
            return []
        return res.fetchall()
