import psycopg2
import connect
import models


cur, conn = connect.db_connect()

all_users = models.get_all_users(cur)

with open("all_users.txt", "w") as w:
    for user in all_users:
        w.write(user.uid)
        w.write(",")
        w.write(user.uname)
        w.write(",")
        w.write(user.i1)
        w.write(",")
        w.write(user.i2)
        w.write(",")
        w.write(user.i3)
        w.write("\n")
