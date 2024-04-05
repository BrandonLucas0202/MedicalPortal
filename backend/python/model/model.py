from database.sqlconnection import SQLConnection
from mysql.connector.cursor import MySQLCursor

class Model():
    
    def __init__(self, table: str, fields: list, primaries: dict) -> None:
        self.__table = table
        self.__fields = fields
        self.__primaries = primaries

    def create(self, database: SQLConnection, data: dict):
        """
        Creates the model into the database with the provided data
        """
        keys = [key for key in data.keys() if key in self.__fields]
        values = [data.get(key) for key in keys]

        if not len(keys) == len(self.__fields):
            return

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    f"INSERT INTO {self.__table.split(' ')[0]} ({', '.join(keys)}) VALUES ({', '.join(['%s' for _ in values])})",
                    values
                )
            connection.commit()

    def update(self, database: SQLConnection, data: dict):
        """
        Updates the model into the database with the provided data
        """
        keys = [key for key in data.keys() if key in self.__fields]
        values = [data.get(key) for key in keys]

        if len(keys) == 0:
            return

        primaryKeys = list(self.__primaries.keys())
        primaryValues = [self.__primaries.get(key) for key in primaryKeys]

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    f"UPDATE {self.__table.split(' ')[0]} SET {', '.join(key + '=%s' for key in keys)} WHERE {' AND '.join(key + '=%s' for key in primaryKeys)}",
                    values + primaryValues
                )
            connection.commit()

    def get(self, database: SQLConnection, filter: dict = None, groupBy:list = None, orderBy: list = None) -> dict:
        """
        Uses the provided database connection and retrieves the data.
        """
        if filter:
            primaryKeys = list(filter.keys())
            primaryValues = [filter.get(key) for key in primaryKeys]
        else:
            primaryKeys = list(self.__primaries.keys())
            primaryValues = [self.__primaries.get(key) for key in primaryKeys]

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = f"SELECT {', '.join(self.__fields)} FROM {self.__table} WHERE {' AND '.join(key + '=%s' for key in primaryKeys)}"
                if groupBy:
                    query+=f" GROUP BY {','.join(groupBy)}"
                if orderBy:
                    query+=f" ORDER BY {','.join(orderBy)}"
                cursor.execute(
                    query,
                    primaryValues
                )

                row = cursor.fetchone()
                if not row:
                    return {}
                
                if len(self.__fields) == 1:
                    result = list(row.values())[0]
                else:
                    result = row

        return result
    
    def getMany(self, database: SQLConnection, filter: dict = None, groupBy:list = None, orderBy: list = None) -> list[dict]:
        """
        Uses the provided database connection and retrieves the data.
        """
        if filter:
            primaryKeys = list(filter.keys())
            primaryValues = [filter.get(key) for key in primaryKeys]
        else:
            primaryKeys = list(self.__primaries.keys())
            primaryValues = [self.__primaries.get(key) for key in primaryKeys]

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = f"SELECT {', '.join(self.__fields)} FROM {self.__table} WHERE {' AND '.join(key + '=%s' for key in primaryKeys)}"
                if groupBy:
                    query+=f" GROUP BY {','.join(groupBy)}"
                if orderBy:
                    query+=f" ORDER BY {','.join(orderBy)}"
                cursor.execute(
                    query,
                    primaryValues
                )
                
                result = []
                for row in cursor:
                    if len(self.__fields) == 1:
                        result.append(list(row.values())[0])
                    else:
                        result.append(row)

        return result

    def delete(self, database: SQLConnection):
        """
        Uses the provided database connection and retrieves the data.
        """
        primaryKeys = list(self.__primaries.keys())
        primaryValues = [self.__primaries.get(key) for key in primaryKeys]

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"DELETE FROM {self.__table.split(' ')[0]} WHERE {' AND '.join(key + '=%s' for key in primaryKeys)}",
                    primaryValues
                )
            connection.commit()

class Searchable():

    def search(self, database: SQLConnection, filter: dict) -> list[dict]:
        """
        Uses the provided database connection and retrieves the data.
        """
        primaryKeys = list(filter.keys())
        primaryValues = [filter.get(key) for key in primaryKeys if key in self.__fields]

        # Get connection and cursor
        with database.connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    f"SELECT {', '.join(self.__fields)} FROM {self.__table} WHERE {' AND '.join(key + 'LIKE %s' for key in primaryKeys)}",
                    primaryValues
                )
                
                result = []
                for row in cursor:
                    entry = {}
                    for field in self.__fields:
                        entry[field] = row[field]
                    result.append(entry)


        return result

class StaticModel(Model):
    
    def update(self, database: SQLConnection):
        pass

class PermanentModel(StaticModel):

    def delete(self, database: SQLConnection):
        pass

class QueryModel(PermanentModel):

    def create(self, database: SQLConnection, data: dict):
        pass