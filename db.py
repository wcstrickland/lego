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

def insert_user(cur, conn, name, item_list):
    uid = str(uuid.uuid4())
    stmt = f"INSERT INTO users(id, uname, item1, item2, item3) VALUES(%s,%s,%s,%s,%s)"
    vals = (uid, name, item_list[0],item_list[1],item_list[2])
    try:
        cur.execute(stmt, vals)
        conn.commit()
        cur.close()
        print("Insert successful!")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: ", error)
    finally:
        if conn is not None:
            conn.close()
#TODO
#def update_user(cur, conn, uid, item_list):
#    usr = select * from users where uid == uid
#    stmt = f"update user blah blah (item1,item2,item3) values(%s,%s,%s)"
#    try:
#        update
#    except (Exception, pyscopg2.DatabaseError) as error:
#        print("Error: ", error)
#    finally:
#        if conn is not None:
#            conn.close()
    




if __name__ == '__main__':
    pass
#    conn, cur = db_connect()
#    name1 = "bill"
#    bill_items = ('999/999', '000/000', '555/555')
#    insert_user(cur, conn, name1, bill_items)
