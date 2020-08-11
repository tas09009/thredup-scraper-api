import requests, re
from bs4 import BeautifulSoup
import sys
# from selenium import webdriver
# from lxml import etree
# import lxml.html
# import urllib.request

# ------------------------------------------------------------------------------------
'''
Input: 
- url: searched items

Output:
- href_list: links of all products on all pages (50 links/page) 
- soupified_list: beautiful soup object (parsed html) of each link within href_list
'''

url = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true&sort=newest_first&page='


product_list = []
href_list = []
soupified_list = []

for page_number in range(1,2): # Everytime range increases, items increase by 50
    url_page = ((url) + str(page_number))

    # Parse HTML and pull all href links
    response = requests.get(url_page)
    soup = BeautifulSoup(response.text, 'html.parser')

    grid_products = soup.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
    for i in grid_products:
        product = i.find('a', {'class': '_1di0il_2VkBBwWJz9eDxoJ'}).get('href')
        product_list.append(product)

# ------------------------------------------------------------------------------------
print('Creating "href_list"')

url_front = 'https://www.thredup.com'
for a in product_list:
    href_list.append(url_front + a)


# Export href_list
original_stdout_href_list = sys.stdout # Save a reference to the original standard output

with open('href_list.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(href_list)
    sys.stdout = original_stdout_href_list # Reset the standard output to its original value
print('Exported "href_list"')

# ------------------------------------------------------------------------------------
print('Creating "soupified_list"')

for link in href_list:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    soupified_list.append(str(soup))


# Export soupified_list
original_stdout_soupified_list = sys.stdout # Save a reference to the original standard output

with open('soupified_list.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(soupified_list)
    sys.stdout = original_stdout_soupified_list # Reset the standard output to its original value
print('Exported "soupified_list"')

# ------------------------------------------------------------------------------------
print('Creating "href_and_soup"')

href_and_soup = dict(zip(href_list, soupified_list))


# Export href_and_soup
original_stdout_href_and_soup = sys.stdout # Save a reference to the original standard output

with open('href_and_soup.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(href_and_soup)
    sys.stdout = original_stdout_href_and_soup # Reset the standard output to its original value
print('Exported "href_and_soup"')


# ------------------------------------------------------------------------------------

'''
url = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true&sort=newest_first&page='

def product_dict():
    
    product_list = []
    href_list = []
    soupified_list = []

    global href_and_soup

    for page_number in range(1,2): # Everytime range increases, items increase by 50
        url_page = ((url) + str(page_number))

        # Parse HTML and pull all href links
        response = requests.get(url_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        grid_products = soup.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
        for i in grid_products:
            product = i.find('a', {'class': '_1di0il_2VkBBwWJz9eDxoJ'}).get('href')
            product_list.append(product)


    url_front = 'https://www.thredup.com'
    for a in product_list:
        href_list.append(url_front + a)



    for link in href_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        soupified_list.append(soup)


    href_and_soup = dict(zip(href_list, soupified_list))
    return href_and_soup


product_dict()
'''

# a_file = open('href_parsed_dict.pkl', 'wb')
# pickle.dump(href_and_soup, a_file)
# a_file.close()

# # Save as json
# json.dump(href_and_soup, open("href_parsed_dict.json", 'w'))

# Save as np
# np.save("href_parsed_dict_np.npy", href_and_soup)

# # Load json
# data = json.load(open("href_parsed_dict.json"))

# # Load np
# read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
# print(read_dictionary['hello']) # displays "world"