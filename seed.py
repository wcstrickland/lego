import uuid
import psycopg2
import db
import models

conn, cur = db.db_connect()

u1 = models.User(str(uuid.uuid4()), "bill", "888/999", "333/222", "444/666")
u1.insert(cur, conn)

u2 = models.User(str(uuid.uuid4()), "connor", "333/333", "999/999", "121/121")
u2.insert(cur, conn)


cur.close()
conn.close()

