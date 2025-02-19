from api.services.mysql.connection import MySQL


def getTables():
    mysql = MySQL()

    try:
        mysql.connect()

        return
    except Exception as e:
        print(e)

    finally:
        mysql.close_connection()