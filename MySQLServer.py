# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # ✅ Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔧 Replace this with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # ✅ NO SELECT or SHOW used
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # ✅ Handle any MySQL-related errors
        print(f"Error: {err}")

    finally:
        # ✅ Ensure cleanup
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
