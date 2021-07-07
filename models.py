
import uuid
import psycopg2


class User:
    def __init__(self, uid, uname, i1, i2, i3):
        self.uid = uid
        self.uname = uname
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)


    def update(self, i1,i2,i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def insert(self, cur, conn):
        stmt = f"INSERT INTO users(uid, uname, item1, item2, item3) VALUES(%s,%s,%s,%s,%s)"
        vals = (self.uid, self.uname, *self.items)
        try:
            cur.execute(stmt, vals)
            conn.commit()
            print("Insert successful!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("User.insert Error: ", error)


class StockReport:
    def __init__(self, uid, uname, i1, i2, i3):
        self.uid = uid
        self.uname = uname
        # each item is a dict{"item": , "status": str(bool)}
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def update(self, i1,i2,i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def insert(self, cur, conn):
        drop_statement = f"drop table if exists {self.uname}"
        table_statement = f"create table {self.uname}(item VARCHAR(255), status VARCHAR(255))"    
        insert_statement = f"insert into {self.uname} (item, status) VALUES (%s, %s)"
        try:
            cur.execute(drop_statement)
            cur.execute(table_statement)
            for item in self.items:
                cur.execute(insert_statement, (item["item"], item["status"]))
            conn.commit()
            print("Insert Successufl!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("StockReport.insert Error: ", error)
