import uuid
import psycopg2
import connect
import models

cur, conn = connect.db_connect()

drop_stmt = "drop table if exists users"
create_stmt = "create table users(uid varchar(255),uname varchar(255),item1 varchar(255),item2 varchar(255),item3 varchar(255))"

cur.execute(drop_stmt)
print("table dropped")
cur.execute(create_stmt)
print("table created")

u1 = models.User(str(uuid.uuid4()), "bill", "888/999", "333/222", "444/666")
u1.insert(cur, conn)
u1.print()

u2 = models.User(str(uuid.uuid4()), "connor", "333/333", "999/999", "121/121")
u2.insert(cur, conn)
u2.print()

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
u1_results = [si1, si2, si3]

u1_stock = models.StockReport(u1.uid, u1.uname, *u1_results)
u1_stock.insert(cur, conn)


si1 = {
    "item": "333/333",
    "status": "true"
}
si2 = {
    "item": "999/999",
    "status": "false"
}
si3 = {
    "item": "121/121",
    "status": "false"
}
u2_results = [si1, si2, si3]

u2_stock = models.StockReport(u2.uid, u2.uname, *u2_results)
u2_stock.insert(cur, conn)

u1_stock_report = u1.get_stock_report(cur)
u1_stock_report.print()

tables = models.get_all_reports(cur)
for stock_report in tables:
    stock_report.print()

cur.close()
conn.close()

