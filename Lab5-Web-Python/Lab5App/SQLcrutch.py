import pymysql
import datetime


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.password = password
        self.host = host
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Task:
    def __init__(self, db_connection, name, description, date):
        self.db_connection = db_connection.connection
        self.name = name
        self. description = description
        self.date = date

    def save(self):
        c = self.db_connection.cursor()
        c.execute("Insert into lab5app_task (name, description, competition_date) values (%s, %s, %s);",
                  (self.name, self.description, self.date))
        self.db_connection.commit()
        c.close()


def delete_task(db_connection, *ids):
    c = db_connection.connection.cursor()
    for t_id in ids:
        c.execute("Delete from lab5app_task where id=%s;", (t_id,))
    db_connection.connection.commit()
    c.close()


con = Connection('dbuser', '123', 'Task_Manager_DB')

with con:
    #delete_task(con, 3)
    task = Task(con, 'Ещё одна задача', 'Описание этой задачи', datetime.datetime.now())
    task.save()
