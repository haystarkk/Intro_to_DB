# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔧 Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # ✅ Only allowed statement: CREATE DATABASE IF NOT EXISTS
            create_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            cursor.execute(create_query)
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        # ✅ Handle MySQL errors
        print(f"Error while connecting to MySQL or creating the database: {err}")

    except Exception as e:
        # ✅ Handle general Python errors
        print(f"Unexpected error: {e}")

    finally:
        # ✅ Cleanup resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
