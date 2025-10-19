import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1:3306",
    user="root",
    password="0404Vera#",
    database="alx_book_store"
)

print(f"Database {mydb.database} created successfully!")