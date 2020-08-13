import requests, re
from bs4 import BeautifulSoup
import sys

# Need all 3?
from href_list import href_list_1
from soupified_list import soupified_list_1
from soupified_list import soupified_list_1
from soupified_list_not_string import soupified_list_not_string_1


# from selenium import webdriver
# from lxml import etree
# import lxml.html
# import urllib.request

# ------------------------------------------------------------------------------------

# def image_scrape(): # Could use url as a parameter...
#     '''
#     Scrape all hrefs of images for 1 item in a search result: 
#     '''
image_list = []

# for href in href_list:
# Parse HTML and pull all href links
# response = requests.get(href_list_1[0])
# soup = BeautifulSoup(response.text, 'html.parser')

# print(type((response))) # <class 'requests.models.Response'>
# print(type(soup)) # <class 'bs4.BeautifulSoup'>

image_grid = (soupified_list_1[0]).findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
for i in image_grid:
    image_href = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
    image_list.append(image_href)
    # return image_list

print(image_list) # <class 'list'>
# image_scrape()


# ------------------------------------------------------------------------------------

# def image_scrape(): # Could use url as a parameter...
#     '''
#     Scrape all hrefs of images for 1 item in a search result: 
#     '''
#     global image_scrape_list

#     image_scrape_list = []


#     for href in soupified_list_1:
#     # Parse HTML and pull all href links
#         # response = requests.get(list_link[href])
#         soup = BeautifulSoup((soupified_list_1[href]).text, 'html.parser')

#         image_grid = soup.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
#         for image in image_grid:
#             image_href = image.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
#             image_scrape_list.append(image_href)
#         return image_scrape_list
# # print(image_scrape())

# image_scrape()
# print(image_scrape_list[0])


# print(type(str(soupified_list_not_string_1[0])))
# print(type(soupified_list_1[0]))


# print(href_list_1[4])








# values = soupified_list_1()
# values_list = list(values)

# a_value = values_list[0]

# print(a_value)





