import uuid
import psycopg2
import connect
import models
import random

def clear_all_reports(cur):
    users = models.get_all_users(cur)
    success = 0
    fail = 0
    count = 0
    for user in users:
        count += 1
        try:
            cur.execute(f"drop table if exists {user.uname}")
            success += 1
        except:
            print(f"something went wrong deleting {user.uname} table\nPerhaps they dont have a table yet?")
            fail += 1
    print(f"Done clearing reports: {success} and deleted, {fail} errors, {count - (success + fail)} not present")

def clear_all_users(cur):
    drop_stmt = "drop table if exists users"
    create_stmt = "create table users(uid varchar(255),uname varchar(255),item1 varchar(255),item2 varchar(255),item3 varchar(255))"
    cur.execute(drop_stmt)
    print("table dropped: All users cleared ")
    cur.execute(create_stmt)
    print("table created: Blank users table ready. ")
    

    

cur, conn = connect.db_connect()

clear_all_users(cur)
clear_all_reports(cur)



name_choices = ["james", "kate", "pat", "tyler", "justin", "jason", "anthony", "caroline", "april", "josh", "armstrong", "hamid", "pickles"]

item_choices = ["8999/2343434", "999/999","2323434/23413133", "1111/111", "8823848348/123213312",  "222/2222", "6253170/61252", "6284589/35381", "6247895/24307", "6226927/23405", "6223171/99206", "6220561/30166"]

for i in range(20):
    rand_name = random.choice(name_choices) + str(random.randint(0, 999))
    rand_items = (random.choice(item_choices),random.choice(item_choices),random.choice(item_choices))
    user = models.User(str(uuid.uuid4()), rand_name, *rand_items)
    user.insert(cur, conn)

users = models.get_all_users(cur)
for i, user in enumerate(users):
    print("\n", i, ': ')
    user.print()
    


cur.close()
conn.close()
