# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    cursor = None

    try:
        # Try connecting to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔧 Replace with your actual password
        )

        # Check if connection is successful
        if connection.is_connected():
            cursor = connection.cursor()

            # ✅ Creating the database (NO SELECT or SHOW used)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"❌ Failed to connect or execute query: {err}")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

    finally:
        # ✅ Close cursor and connection properly
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
