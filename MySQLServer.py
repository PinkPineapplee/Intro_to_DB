import mysql.connector
from mysql.connector import Error


def create_alx_book_store_db():
    mydb = None
    cursor = None
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="0404Vera#",
        )

        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            cursor.execute("USE alx_book_store")
            print(f"Database {mydb.database} created successfully!")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if cursor is not None:
            cursor.close()
        if mydb is not None and mydb.is_connected():
            mydb.close()


if __name__ == "__main__":
    create_alx_book_store_db()