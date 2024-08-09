from connect_gym_database import connect_gym_database as connect_db
from mysql.connector import Error
import datetime
conn = connect_db()

def add_member(name, age):
    try:
        cursor = conn.cursor
        query = 'INSERT INTO members (name,age) VALUES (%s,%s)'
        cursor.execute(query,(name,age))
        conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unknown Error: {e}')
    else:
        print(f'User {name} added succsesfully!')

def add_workout_session(member_id, duration_minutes, calories_burned):
    try:
        date = datetime.datetime.now()
        cursor = conn.cursor()
        query = 'INSERT INTO workout_sessions (member_id,date,duration_minutes,calories_burned) VALUES (%s,%s,%s,%s)'
        cursor.execute(query,(member_id,date,duration_minutes,calories_burned))
        conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unknown Error: {e}')
    else:
        print('Workout session added!')

def update_member_age(member_id, new_age):
    try:
        cursor = conn.cursor()
        query = 'UPDATE members SET age = %s WHERE id = %s'
        cursor.execute(query,(new_age,member_id))
        conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unknown Error: {e}')
    else:
        print('Updates user age!')

def delete_workout_session(session_id):
    try:
        cursor = conn.cursor()
        query = f'DELETE workout_sessions WHERE id = {session_id}'
        cursor.execute(query)
        conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unknown Error: {e}')
    else:
        pass

