# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔧 Replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # ✅ No SELECT or SHOW — only CREATE DATABASE
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Close cursor
            cursor.close()

    except Error as err:
        print(f"Error: {err}")

    finally:
        # Ensure the connection is closed
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
