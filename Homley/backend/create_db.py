import pymysql
import os

host = '127.0.0.1'
user = 'root'
password = ''
port = 3306

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        port=port
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS homely")
        print("Database 'homely' created successfully (or already exists).")
    connection.close()
except Exception as e:
    print(f"Failed to create database: {e}")
