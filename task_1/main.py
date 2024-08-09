import gym_database_managment as gymdb

if __name__ == '__main__':
    if gymdb.connect_db() is not None:
        gymdb.add_member('Tim',18,)
        gymdb.add_workout_session(1,60,300,)
        gymdb.update_member_age(6,19)
