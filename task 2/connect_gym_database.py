import mysql.connector as connector

database_name = 'gym_db'
user_name = 'root'
user_password = 'password'
host = 'localhost'

def connect_gym_database():
    try:
        conn = connector.connect(
            database = database_name,
            user = user_name,
            password = user_password,
            host = host
        )
        return conn
    except connector.Error as e:
        print(f'Could not connet to database: {e}')
        return None