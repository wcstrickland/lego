import uuid
import psycopg2
from db_config import opts


def db_connect():
    params = opts
    print("Connecting to Postgres DB")    
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT version()")
        print(cur.fetchone())
        print("Database connected:")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn, cur


def get_all_users(cur):
    cur.execute("SELECT * FROM lego")
    rows = cur.fetchall()
    cur.close()
    return rows




if __name__ == '__main__':
    pass
#    conn, cur = db_connect()
#    name1 = "bill"
#    bill_items = ('999/999', '000/000', '555/555')
#    insert_user(cur, conn, name1, bill_items)
