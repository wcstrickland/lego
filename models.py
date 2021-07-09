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
#            print(f"\nInsert {self.uname} successful!\n")
        except (Exception, psycopg2.DatabaseError) as error:
            with open("error_log.txt", "a") as f:
                f.write(f"{self.uname} User.insert Error: ", error)


    def get_stock_report(self, cur):
        try:
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
        except (Exception, psycopg2.DatabaseError) as error:
            with open("error_log.txt", "a") as f:
                now  = datetime.now()
                fmt_time = now.strftime("%H:%M:%S  %m-%d-%Y")
                print(f"{fmt_time} : {self.uname} get_stock_report Error: ", error, file = f)
        




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
        print(f"\nid: {self.uid}\nname: {self.uname}\n")
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
#            print("Insert Successful!")
        except (Exception, psycopg2.DatabaseError) as error:
            with open("error_log.txt", "a") as f:
                now  = datetime.now()
                fmt_time = now.strftime("%H:%M:%S  %m-%d-%Y")
                print(f"{fmt_time} : {self.uname} StockReport.insert Error: ", error, file = f )


def get_all_users(cur):
    users = []
    cur.execute("SELECT * FROM users")
    # it may be tempting to use fetchall() and use a list comp. Dont!
    # any error will cause a halt over the rest of result set.
    while True:
        row = cur.fetchone()
        if row:
            user = User(*row)
            users.append(user)
        else:
            break
    return users


def get_all_reports(cur, conn):
    tables = []
    users = get_all_users(cur)
    for user in users:
        cur = conn.cursor()
        stock_report  = user.get_stock_report(cur)
        tables.append(stock_report)
    return tables
        
