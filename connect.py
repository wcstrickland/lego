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
        print("error connecting to db : ", error)
    return cur, conn

