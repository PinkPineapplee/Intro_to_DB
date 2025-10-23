import mysql.connector
from mysql.connector import Error



def execute_safe_sql(cursor, query):
    """Check query before running it """
    lower_query = query.lower().strip()

    if lower_query.startswith("select") or lower_query.startswith("show"):
        print(" Error : 'SELECT' and 'SHOW' statements are not allowed.")
        return

    try:
        cursor.execute(query)
        print(f"✅ Executed: {query}")
    except mysql.connector.Error as e:
        print(f"⚠️ MySQL Error while executing query: {e}")



def create_database():   
    mydb = None
    cursor = None    
    try:
            mydb = mysql.connector.connect(
                    host = "127.0.0.1",
                    port = 3306,
                    user = "root",
                    password = "0404Vera#"
                    )


            if mydb.is_connected():
                cursor = mydb.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                cursor.execute("USE alx_book_store")
                print("Database 'alx_book_store' created successfully!")
                 # Test the rule:
                execute_safe_sql(cursor, "SELECT * FROM test_table;")   # blocked
                execute_safe_sql(cursor, "SHOW DATABASES;")             # blocked
                execute_safe_sql(cursor, "CREATE TABLE IF NOT EXISTS test_table (name VARCHAR(50));")  # allowed
                execute_safe_sql(cursor, "INSERT INTO test_table (name) VALUES ('Vera');")             # allowed

                mydb.commit()
    except mysql.connector.Error as e:
        print(f"MySQL Error: {e}")

    except Exception as e:
        print(f"General Error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if mydb is not None and mydb.is_connected():
            mydb.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()