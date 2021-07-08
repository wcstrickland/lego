import psycopg2
from datetime import datetime

class User:


    def __init__(self, uid, uname, i1, i2, i3):
        self.uid = uid
        self.uname = uname
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def print(self):
        print(f"\nid: {self.uid}\nname: {self.uname}\n items: {self.items}")


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


    def get_stock_report(self, cur):
        stmt = f"SELECT * FROM {self.uname}"
        cur.execute(stmt)
        items = []
        rows = cur.fetchall()
        for row in rows:
            item = {}        
            item["item"] = row[0]
            item["status"] = row[1]
            items.append(item)
        return StockReport(self.uid, self.uname, *items)
        




class StockReport:
    def __init__(self, uid, uname, i1, i2, i3):
        self.uid = uid
        self.uname = uname
        # each item is a dict{"item": , "status": str(bool)}
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def print(self):
        print(f"\nid: {self.uid}\nname: {self.uname}")
        for item in self.items:
            print(item)


    def update(self, i1,i2,i3):
        self.i1 = i1
        self.i2 = i2
        self.i3 = i3
        self.items = (self.i1, self.i2, self.i3)

    def insert(self, cur, conn):
        drop_statement = f"drop table if exists {self.uname}"
        table_statement = f"create table {self.uname}(item VARCHAR(255), status VARCHAR(255), check_time VARCHAR(255))"    
        insert_statement = f"insert into {self.uname} (item, status, check_time) VALUES (%s, %s, %s)"
        now  = datetime.now()
        fmt_time = now.strftime("%H:%M:%S")
        try:
            cur.execute(drop_statement)
            cur.execute(table_statement)
            for item in self.items:
                cur.execute(insert_statement, (item["item"], item["status"], fmt_time))
            conn.commit()
            print("Insert Successful!")
        except (Exception, psycopg2.DatabaseError) as error:
            print("StockReport.insert Error: ", error)


def get_all_users(cur):
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows

def get_all_reports(cur):
    tables = []
    rows = get_all_users(cur)
    for row in rows:
        user = User(*row)
        stock_report  = user.get_stock_report(cur)
        tables.append(stock_report)
    return tables
        

        
