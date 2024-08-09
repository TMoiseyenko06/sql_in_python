from connect_gym_database import connect_gym_database as connect_db
from mysql.connector import Error
conn = connect_db()

def get_members_in_age_range(start_age, end_age):
    try:
        cursor = conn.cursor()
        query = 'SELECT * FROM members WHERE age BETWEEN %s and %s'
        cursor.execute(query,(start_age,end_age))
        conn.commit()
    except Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Unknown Error: {e}')
    else:
        pass