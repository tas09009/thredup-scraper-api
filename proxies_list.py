import requests, re
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
import scrapy-rotating-proxies
# import pandas as pd
# import timeit
# from href_list import href_list_1
# import sys
# from fake_useragent import UserAgent



# a = range(10) 
# b = [] 
# for looping in a:     
#     b.append(looping*2)
#     print('Completed {i}/50 items'.format(i=looping))

# b = []
# for looping in href_list_1:
#      b.append(looping)
# print('Completed {number}/50 items'.format(number=looping))
# print(b[4])

# Source: https://towardsdatascience.com/web-scraping-with-python-a-to-copy-z-277a445d64c7

def proxies_pool():
    url = 'https://www.sslproxies.org/'
    
    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
    with requests.Session() as res:
        proxies_page = res.get(url)
        
    # Create a BeutifulSoup object and find the table element which consists of all proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')
  
    # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
    return proxies
# print(proxies_pool())

ROTATING_PROXY_LIST = proxies_pool()


# Source: https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/

proxies = proxies_pool()
proxy_pool = cycle(proxies)

url = 'https://httpbin.org/ip'
for i in range(1,11):
    #Get a proxy from the pool
    proxy = next(proxy_pool)
    print("Request #%d"%i)
    try:
        response = requests.get(url,proxies={"http": proxy, "https": proxy})
        print(response.json())
    except:
        #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
        #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
        print("Skipping. Connnection error")




