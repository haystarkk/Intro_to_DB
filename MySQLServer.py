# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def contains_disallowed_keywords(query):
    """
    Check if the SQL query contains SELECT or SHOW keywords.
    """
    disallowed_keywords = ['SELECT', 'SHOW']
    upper_query = query.upper()
    for keyword in disallowed_keywords:
        if keyword in upper_query:
            return True
    return False

def create_database():
    connection = None
    cursor = None

    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'  # 🔧 Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create database
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # ✅ Check for disallowed SQL keywords
            if contains_disallowed_keywords(create_db_query):
                print("❌ Error: SELECT or SHOW statements are not allowed in the SQL query.")
                return

            # ✅ Execute the safe query
            cursor.execute(create_db_query)
            print("✅ Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"❌ MySQL error: {err}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        # ✅ Clean resource closure
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
