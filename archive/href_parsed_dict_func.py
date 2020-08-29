import requests, re
from bs4 import BeautifulSoup
import sys

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

for page_number in range(1,2): # Everytime range increases, items increase by 50. Ordered by "Newest first"
    url_page = ((url) + str(page_number))

    # Parse HTML and pull all href links
    response = requests.get(url_page)
    main_page_items = BeautifulSoup(response.text, 'html.parser')

    grid_products = main_page_items.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
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
    product_page = BeautifulSoup(response.text, 'html.parser')
    soupified_list.append(product_page)


# Export soupified_list
original_stdout_soupified_list = sys.stdout # Save a reference to the original standard output

with open('soupified_list.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(soupified_list)
    sys.stdout = original_stdout_soupified_list # Reset the standard output to its original value
print('Exported "soupified_list"')

# ------------------------------------------------------------------------------------
print('Creating "href_and_soup_dict"')

href_and_soup_dict = dict(zip(href_list, soupified_list))


# Export href_and_soup_dict
original_stdout_href_and_soup = sys.stdout # Save a reference to the original standard output

with open('href_and_soup_dict.py', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(href_and_soup_dict)
    sys.stdout = original_stdout_href_and_soup # Reset the standard output to its original value
print('Exported "href_and_soup_dict"')


# ------------------------------------------------------------------------------------
