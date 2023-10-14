import psycopg2
from config import *

try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = False
    with connection.cursor() as cursor:
        # cursor.execute(
        #     '''CREATE TABLE footballers(
        #     id serial PRIMARY KEY,
        #     name varchar(25) NOT NULL,
        #     year integer,
        #     team varchar(25) NOT NULL,
        #     height real);
        #     '''
        # )
        # print('[INFO] Table created')

        def insert_footballers(lst):
            cursor.execute(
                f"""INSERT INTO footballers (id, name, year, team, height)
                    VALUES {lst}
                """
            )
        def get_footballers():
            cursor.execute(
                """SELECT * from footballers"""
            )
            rows = cursor.fetchall()
            for i in rows:
                print(i)
        def get_footballer(number):
            cursor.execute(
                f"""SELECT * from footballers where id = {number}"""
            )
            rows = cursor.fetchall()
            for i in rows:
                print(i)
        def delete_footballer(number):
            cursor.execute(
                f"""DELETE from footballers where id = {number}"""
            )
        def update_footballer(number, dict):
            cursor.execute(
                f"""UPDATE footballers set team = '{dict["team"]}' where id = {number}"""
            )
            print('[INFO] Information is updated')

        footballer_1 = (1, 'Cristiano Ronaldo', 1985, 'Al Nassr', 1.87)
        footballer_2 = (2, 'Lionel Messi', 1987, 'Inter Miami', 1.70)
        footballer_3 = (3, 'Marcus Rashford', 1997, 'Manchester United', 1.80)
        dict1 = {'id' : 3, "team" : "Real Madrid"}

        # insert_footballers(footballer_1)
        # insert_footballers(footballer_2)
        # insert_footballers(footballer_3)
        # get_footballers()
        # get_footballer(2)
        # delete_footballer(2)
        update_footballer(3, dict1)

        connection.commit()

except Exception as ex:
    print('[INFO] Error while working with PostgreSQL', ex)
    connection.rollback()
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
