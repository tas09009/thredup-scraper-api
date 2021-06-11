import requests, re
from bs4 import BeautifulSoup
# from selenium import webdriver
from lxml import etree
import lxml.html
import urllib.request

url = 'https://www.thredup.com/petite?department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&sort=newest_first&page=1'

# Parse HTML and pull all href links
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')




# ------------------------------------------------------------------------------------

def product_href_scrape(): # Could use url as a parameter...
    '''
    Scrape all products's url in a search result: 
    '''

    url = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&include_petite=true&sort=newest_first&skip_equivalents=true&redirectPath=%2Fsaved&page='

    product_list = []
    
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
    list_link = [url_front + a for a in product_list]
    return list_link 
# print(len(product_href_scrape()))







def image_scrape(): # Could use url as a parameter...
    '''
    Scrape all hrefs of images for 1 item in a search result: 
    '''

    url3 = 'https://www.thredup.com/product/women-polyester-worthington-blue-short-sleeve-blouse/75338788?sizing_id=755,765,750,756,791,799,774,778'

    image_list = []

    # Parse HTML and pull all href links
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.text, 'html.parser')

    image_grid = soup3.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
    for i in image_grid:
        image_href = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
        image_list.append(image_href)
    return image_list
# print(image_list)



def materials_scrape():
    '''
    Scrape Material's info from a page
    '''
    url4 = 'https://www.thredup.com/product/women-cotton-dressbarn-gray-cardigan/73718533?sizing_id=755,765,778,750,756,774,791,799'

    # Parse HTML and pull all href links
    response4 = requests.get(url4)
    soup4 = BeautifulSoup(response4.text, 'html.parser')

    product_item = []
    product_list_major = []

    grid_category = soup4.findAll('div', {'class': '_2SuzvN3bcsWRtNcNiSLMGq'})
    for i in grid_category:
        product = i.find('p')
        product_item.append(product)

    item = str(product_item[1])[3:-4]
    product_list_major.append(item)
    return product_list_major
# print(product_list_major)


def size_and_measurement():
    '''
    ['Size S '] removes the word 'petite' as well, not needed
    ['24" Length']
    '''

    url4 = 'https://www.thredup.com/product/women-cotton-dressbarn-gray-cardigan/73718533?sizing_id=755,765,778,750,756,774,791,799'

    # Parse HTML and pull all href links
    response4 = requests.get(url4)
    soup4 = BeautifulSoup(response4.text, 'html.parser')

    product_item = []

    grid_category = soup4.findAll('ul', {'class': 'list-disc'})
    for i in grid_category:
        product = i.findAll('li')
        product_item.append(product)

    size = []
    measurements = []

    item = product_item[1]
    size.append(str(item[0])[4:-13])
    measurements.append(str(item[1])[4:-5])
    return size, measurements

# print(size)
# print(measurements)
# print(size_and_measurement())


def category_type():
    '''
    ['Size S '] removes the word 'petite' as well, not needed
    ['24" Length']
    '''

    url4 = 'https://www.thredup.com/product/women-cotton-dressbarn-gray-cardigan/73718533?sizing_id=755,765,778,750,756,774,791,799'

    # Parse HTML and pull all href links
    response4 = requests.get(url4)
    soup4 = BeautifulSoup(response4.text, 'html.parser')

    product_type = []

    grid_category = soup4.findAll('nav', {'class': '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'})
    for i in grid_category:
        product = i.find('a', {'class': 'spot-grey-7 JdCj53-vTvU5pLpj6NlFo'}).getText()
        product_type.append(product)
    return product_type
print(category_type())


# ------------------------------------------------------------------------------------

# LATER



def category_scrape(): #Does this need to be a function? Just a for loop?
    '''
    Scrape all main clothing categories: Dresses, tops, sweaters, etc.
    '''

    category_list = []

    grid_category= soup.findAll('li', {'class': '_1ZkzHFB3fpqNDvSNYgP3Jr'})
    for i in grid_category:
        category = i.find('a', {'class': 'u-display-block'}).get('data-label')
        category_list.append(category)
    return(category_list)
# print(category_scrape())



def category_urls():
    '''
    list of urls for each clothing category in "category list". Ex: dresses, tops, sweaters, etc.
    '''
    category_list = ['All Petite', 'Dresses', 'Tops', 'Sweaters', 'Coats & Jackets', 'Jeans', 'Pants', 'Skirts', 'Shorts', 'Activewear', 'Swimwear'] # Don't use hardcoded list

    # Remove the first item, not needed
    category_list.pop(0)

    # Use category_scrape function in the end
    category_list = [sub.replace('Coats & Jackets', 'Outerwear') for sub in category_list]

    category_list_edit = []
    for lower_item in category_list:
        category_list_edit.append(lower_item.lower())

    # category_list_edit = ['dresses', 'tops', 'sweaters', 'outerwear', 'jeans', 'pants', 'skirts', 'shorts', 'activewear', 'swimwear']

    url_categories = []
    url_split = url.split('?')
    for product in range(len(category_list_edit)):
        url_piece_insert = '/' + category_list_edit[product] + '?search_tags=women-' + category_list_edit[product] + '&'
        url_full = url_split[0] + url_piece_insert + url_split[1]
        url_categories.append(url_full)

    return url_categories
# print(category_urls())



# The two functions below pull all checkbox labels within filter categories within a clothing type:
# Ex: Uses url of "dresses" (within clothing category), to pull all dress related checkboxes

def product_filter_1sthalf():
    '''
    Pulls all product filters: ['Casual', 'Cocktail & Party', 'Formal', etc.]
    '''

    url1 = 'https://www.thredup.com/petite/dresses?search_tags=women-dresses&department_tags=petite&skip_equivalents=true&sizing_id=755%2C765%2C750%2C756%2C791%2C799%2C774%2C778'

    
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.text, 'html.parser')

    product_filter_list = []

    product_filter_category= soup1.findAll('li', {'class': '_1W7Y0K4ryaO-ghLN49qY_C'})
    for i in product_filter_category:
        product_filter = i.find('a', {'class': 'u-display-block'}).get('data-label')
        product_filter_list.append(product_filter)
    return product_filter_list
# print(product_filter_1sthalf())


def pattern_accents_2ndhalf():
    '''
    Parse txt document for "Pattern" + 'Accents' categories: ['Animal Print', 'Argyle', etc.]
    '''

    file_pattern_accents = open('pattern_accents_html.txt', 'r')
    soup1 = BeautifulSoup(file_pattern_accents, 'html.parser')

    pattern_accents_list = []

    pattern_accents_category= soup1.findAll('li', {'class': '_1W7Y0K4ryaO-ghLN49qY_C'})
    for i in pattern_accents_category:
        pattern_accents_filter = i.find('a', {'class': 'u-display-block'}).get('data-label')
        pattern_accents_list.append(pattern_accents_filter)
    return pattern_accents_list    
# print(pattern_accents_2ndhalf())



# To be used later for "description" details
'''
url4 = 'https://www.thredup.com/product/women-cotton-dressbarn-gray-cardigan/73718533?sizing_id=755,765,778,750,756,774,791,799'

# Parse HTML and pull all href links
response4 = requests.get(url4)
soup4 = BeautifulSoup(response4.text, 'html.parser')

product_item = []
product_list_major = []

grid_category = soup4.findAll('ul', {'class': 'list-disc'})
for i in grid_category:
    product = i.findAll('li')
    product_item.append(product)

# item = str(product_item[1])[3:-4]
# product_list_major.append(item)
# return product_list_major
# print(product_list_major)

print(product_item)
'''


# ------------------------------------------------------------------------------------
# IP Addresses

def proxies_pool():
    '''
    Scrapes all IP Addresses from website    
    '''
    
    url = 'https://www.sslproxies.org/'
    
    # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
    with requests.Session() as res: # Do we need session - just use get? Maybe it's becuase it uses the "with"?
        proxies_page = res.get(url)
        
    # Create a BeutifulSoup object and find the table element which consists of all proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')
  
    # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
    return proxies

# print(proxies_pool)


