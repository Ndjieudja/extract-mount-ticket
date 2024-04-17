# --*-- coding:utf8 --*--

import keys
import psycopg2


def connection_to_database(user, mdp, db_name):
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=mdp,
            host="localhost"
        )
        if conn:
            conn.autocommit = True
            cursor = conn.cursor()
            exists = '''
                select * from pg_database where datname='POSTICKET'
            '''
            if not exists:
                command = "CREATE DATABASE POSTICKET"
                cursor.execute(command)
            db_names = cursor.execute('''
                select * from pg_database where datname='POSTICKET'
            ''')
            print(db_names)
            conn.commit()
            cursor.close()
            conn.close()

    except Exception as error:
        print(error)


class CommitTicket:

    def __int__(self, files):
        self.user = keys.USER
        self.mdp = keys.PASSWORD
        self.db_name = keys.DATABASE


if __name__ == '__main__':
    connection_to_database(keys.USER, keys.PASSWORD, keys.DATABASE)

