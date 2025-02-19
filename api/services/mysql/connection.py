import os
import mysql.connector
from mysql.connector import Error
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


class MySQL:
    def __init__(self):
        self.connection: PooledMySQLConnection | MySQLConnectionAbstract | None = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE"),
            )

            if self.connection.is_connected():
                print("Successfully connected to the database")
                return self.connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed")
