import psycopg2
import connect
import models


cur, conn = connect.db_connect()

all_users = models.get_all_users(cur)

with open("all_users.txt", "w") as w:
    for user in all_users:
        w.write(user.uname)
