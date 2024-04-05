"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A MySQL database connection object that handles the connection pool
to the database.
"""
import mysql.connector.pooling as pooling

class SQLConnection():

    def __init__(self, config) -> None:
        # Save the configuration 
        self.__config = config
        # Initialize the connection pool
        self.__pool = pooling.MySQLConnectionPool(pool_name = "backend_pool", pool_size = 10, **self.__config)
        

    def connection(self):
        """Returns a connection from the pool"""
        return self.__pool.get_connection()
    
    