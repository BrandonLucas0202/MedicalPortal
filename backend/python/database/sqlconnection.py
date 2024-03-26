"""
Trevor Sharp
CS-310
Software Engineering II 
Medical Portal

A MySQL database connection object that handles the connection pool
to the database.
"""
import mysql.connector as connector
import mysql.connector.pooling as pooling

class SQLConnection():

    def __init__(self, config) -> None:
        # Save the configuration 
        self.config = config
        # Initialize the connection pool
        self.pool = pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 5, **self.config)
        

    def connection(self):
        """Returns a connection from the pool"""
        return self.pool.get_connection()
    
    