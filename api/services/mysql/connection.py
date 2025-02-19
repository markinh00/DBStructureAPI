import mysql.connector
from mysql.connector import Error


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="your_host",  # e.g., "localhost" or an IP address
            user="your_username",  # e.g., "root"
            password="your_password",  # your MySQL password
            database="your_database"  # your database name
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None


def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")