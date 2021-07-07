import uuid
import psycopg2
import db
import models

conn, cur = db.db_connect()

drop_stmt = "drop table users"
create_stmt = "create table users(uid varchar(255),uname varchar(255),item1 varchar(255),item2 varchar(255),item3 varchar(255))"

cur.execute(drop_stmt)
print("table dropped")
cur.execute(create_stmt)
print("table created")

u1 = models.User(str(uuid.uuid4()), "bill", "888/999", "333/222", "444/666")
u1.insert(cur, conn)

u2 = models.User(str(uuid.uuid4()), "connor", "333/333", "999/999", "121/121")
u2.insert(cur, conn)

si1 = {
    "item": "888/999",
    "status": "true"
}
si2 = {
    "item": "333/222",
    "status": "true"
}
si3 = {
    "item": "444/666",
    "status": "false"
}
results = [si1, si2, si3]

stock = models.StockReport(u1.uid, u1.uname, *results)
stock.insert(cur, conn)

cur.close()
conn.close()

