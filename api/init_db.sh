#! /bin/sh
SQL=".read init.sql"
echo $SQL | sqlite3 develop.db
exit 0
