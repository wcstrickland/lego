import psycopg2
import connect
import models


cur, conn = connect.db_connect()

all_users = models.get_all_users(cur)
all_reports = models.get_all_reports(cur, conn)

for i, user in enumerate(all_users):
    print()
    print(i)
    user.print()

print("*"*80)

if len(all_reports)!=0:
    for i, report in enumerate(all_reports):
        if report:
            print()
            print(i)
            report.print()

cur.close()
conn.close()
