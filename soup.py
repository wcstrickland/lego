#!/usr/bin/env python3
import requests_html
from requests_html import HTMLSession
import bs4

session = HTMLSession()
res = session.get("https://www.lego.com/en-us/page/static/pick-a-brick?query=6348059%2F44842&page=1")
res.html.render()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
