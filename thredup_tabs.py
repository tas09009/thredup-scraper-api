# OBJECTIVE
# Filter out clothing items (thredup.com) by removing items with Materials made of "polyester" 
# or "Fabric details not available"

import requests, time, re, sys, webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.thredup.com/products/petite/dresses?department_tags=petite&search_tags=women-dresses&chars_skirt_dress_name=high%20low&sizing_id=755%2C765%2C756%2C750&skip_equivalents=true&sort=Newest%20First&state=listed'

# url = sys.argv[1]
# print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'> # print(soup.prettify()) # class 'str'

# Find all href links that contain: "_1di0il_2VkBBwWJz9eDxoJ". This element represents each item on the page
list_link_partial = [link['href'] for link in soup.findAll("a", {"class": "_1di0il_2VkBBwWJz9eDxoJ"})]

# Add the front part of the webpage to make a full html link
url_front = 'https://www.thredup.com'
list_link = [url_front + a for a in list_link_partial]
print(list_link)



# Open new tab for each link in list_link unless it contains the "banned" words
for i in range(len(list_link)):


	# Parses new webpage to find Materials
	# url1 = list_link[i]
	response1 = requests.get(url1)
	soup1 = BeautifulSoup(response1.text, "html.parser")
	des_attr = soup1.select("div:nth-child(2) > div:nth-child(9) > p")
	des_attr_text = str(des_attr[0])
 
    print(des_attr_text)

 
    

    # If it contains the "banned" words, print them out. If not, open new tab
    if des_attr_text.find('Polyester') != -1
        print('Polyester')
    elif (des_attr_text.find('Acrylic') != -1):
        print('Acrylic')
    elif (des_attr_text.find('Polyamide') != -1):
        print('Polyamide')
    elif (des_attr_text.find('Fabric details not available') != -1):
        print('Fabric details not available')
    elif (des_attr_text.find('No Fabric Content') != -1):
        print('No Fabric Content')
    else: 
    # webbrowser.open_new(url1)
    # time.sleep(3)
        print('See browser')
        sdfsdfsdf
    sdfsdfsdf
    
    
    

# # CSS Selector: in case website's HTML/CSS changes in the future
# #root > div > main > div > div > section > div:nth-child(2) > div:nth-child(9) > p
