
# OBJECTIVE
# Filter out clothing items (thredup.com) by removing items with Materials made of "polyester" 
# or "Fabric details not available"

import requests, time, re, pprint, sys, webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.thredup.com/products/petite?chars_sleeve_length=short%20sleeve&department_tags=petite&search_tags=women-tops%2Cwomen-tops-button-down-shirts&sizing_id=750%2C755%2C756%2C765&skip_equivalents=true&state=listed'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'> # print(soup.prettify()) # class 'str'

# Find all href links that contain: "_1di0il_2VkBBwWJz9eDxoJ". This element represents each item on the page
list_link_partial = [link['href'] for link in soup.findAll("a", {"class": "_1di0il_2VkBBwWJz9eDxoJ"})]

# Add the front part of the webpage to make a full html link
url_front = 'https://www.thredup.com'
list_link = [url_front + a for a in list_link_partial]

# Open new tab for each link in list_link unless it contains the "banned" words
def open_link(list_link):
	for i in range(len(list_link)):

		# Parses new webpage to find Materials
		url1 = list_link[i]
		response1 = requests.get(url1)
		soup1 = BeautifulSoup(response1.text, "html.parser")
		des_attr = soup1.find('p').getText() # 'Materials' are all under <p> tag

		# If it contains the "banned" words, print them out. If not, open new tab
		if (des_attr.find('Polyester') != -1): 
			print ('Polyester') 
		elif (des_attr.find('Fabric details not available') != -1):
			print ('Fabric details not available')
		elif (des_attr.find('No Fabric Content') != -1):
			print ('No Fabric Content')
		else: 
			webbrowser.open_new(url1)
			time.sleep(3)

open_link(list_link)
