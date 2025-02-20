from api.services.mysql.connection import MySQL
import pandas as pd

def getTables():
    mysql = MySQL()

    try:
        labels = [ "Field", "Type", "Null", "Key", "Default", "Extra" ]
        mysql.connect()
        cursor = mysql.connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            print(f"\nEstrutura da tabela '{table_name}':")
            cursor.execute(f"DESCRIBE {table_name};")
            structure = cursor.fetchall()

            # Convertendo os dados para um DataFrame do pandas
            df = pd.DataFrame(structure, columns=labels, index=None)
            print(df)

        return
    except Exception as e:
        print(e)

    finally:
        mysql.close_connection()