# OBJECTIVE
# Remove "sold" items from favorite's list

import requests, time, re, sys, webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.thredup.com/saved/favorites'

# url1 = sys.argv[1]


# Parses new webpage to find Materials
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup1.prettify)
# des_attr = soup1.select("title")

des_attr = soup.select("div:nth-child(7)")
# for i in des_attr:
#     print(i)
# des_attr_text = str(des_attr[0])

sold = soup.find_all("p")
print(sold)

#root > div > main > div > div > section > div:nth-child(2) > div:nth-child(3) > div._3XVoyjYkztFGE3hTkzO6Sz > div._1eLiFjiuarjFHc_xVyw9IR._2GH9vWMhO8HoxiMFmNZWry > p

#root > div > main > div > div > section > div:nth-child(2) > div:nth-child(7) > div._3XVoyjYkztFGE3hTkzO6Sz > div._1eLiFjiuarjFHc_xVyw9IR._2GH9vWMhO8HoxiMFmNZWry

# Heart to get to favorites
#root > div > header > div._2cvL5abrIJZlPNUuT6nxJR > div > div.u-flex.u-flex-center._1j5PByjOav94tX7nhh_tcz > a.u-flex > svg > path.svg-fill