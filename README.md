# overview

- A program reads from database a User and a list of their desired items
- The program scrapes a website to determine if the desired items are instock
- finally creates a new table associated with the user that records each item's stock status
- cron schedules the scraper to be run on all users' items periodically
- database is meant for consumption by a web app to allow users to input wishlist items and view status
