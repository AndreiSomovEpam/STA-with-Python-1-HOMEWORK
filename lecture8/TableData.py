import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        self.data = self.__execute("SELECT * from " + self.table_name)

    def __len__(self):
        self.__init__(self.database_name, self.table_name)
        return len(self.data.fetchall())

    def __getitem__(self, item):
        self.__init__(self.database_name, self.table_name)
        return self.__execute("SELECT * from " + self.table_name + " WHERE name = '" + item + "'").fetchall()

    def __contains__(self, item):
        self.__init__(self.database_name, self.table_name)
        dd = []
        for d in self.data.fetchall():
            dd.append(d[0])
        return item in dd

    def __iter__(self):
        return self

    def __next__(self):
        row = self.data.fetchone()
        if row is not None:
            return row
        else:
            raise StopIteration

    def __execute(self, query):
        return sqlite3.connect(self.database_name).cursor().execute(query)