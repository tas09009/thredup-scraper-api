import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import timeit
from href_list import href_list_1
import sys
from fake_useragent import UserAgent


basic_scrape = {
     'Link': ['heythere', 'test'],
     'Image_link': ['image_list', 'test'],
     'Materials': ['product_list_major', 'test'],
     'Size': ['size', 'test'],
     'Measurements': ['measurements', 'test'],
     'Category_List': ['category_list', 'test']
}

# df = pd.DataFrame.from_dict(basic_scrape)


# df.to_csv(r'/home/taniya/Projects/Thredup-database/basic_scrape.csv', index=False, header=True)



# a = range(10) 
# b = [] 
# for looping in a:     
#     b.append(looping*2)
#     print('Completed {i}/50 items'.format(i=looping))

b = []
for looping in href_list_1:
     b.append(looping)
# print('Completed {number}/50 items'.format(number=looping))
# print(b[4])



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





import requests
url = 'https://httpbin.org/ip'
proxies = {
    "http": 'http://194.44.225.34:53281', 
    "https": 'http://194.44.225.34:53281'
}
response = requests.get(url,proxies=proxies)
# print(response.json())

print('hello')