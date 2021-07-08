# scrape
- [x] figure out the query string for the search
- [x] make a function that takes an item number and produces a query string
- [x] use a web driver that can handle react/angular
- [ ] ~~Email notification?~~
- [x] database schema?
- [ ] cron?
- [x] requirements.txt
- [x] postgres?
- [ ] ~~command line arguments for searches or~~ user record in db/

## TODO
- [x] change get_all_records from fetchall() to fetchone() with iteration to pevent error cascade blocking the transaction
- [x] log errors to a file rather than stdout
- [ ] create script to copy log file out if it is too large
- [ ] python script to fetch all users and print to file. Then split that file. Cron jobs to run main and get input from each split file.
- [ ] each file will be the source for queries
