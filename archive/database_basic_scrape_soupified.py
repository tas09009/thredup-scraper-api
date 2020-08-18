import requests, re
from bs4 import BeautifulSoup



# from selenium import webdriver
# from lxml import etree
# import lxml.html
# import urllib.request

# ------------------------------------------------------------------------------------

'''
Sizes being used in this program:
XXS, XS, SM
00, 0, 2
28, 29

Exclude One size
'''


# url needs to be sorted by newest first
url = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true&sort=newest_first&page='


# ------------------------------------------------------------------------------------

keys_list = list(href_dict)
a_key = keys_list[3]

print(a_key)

values = href_dict.values()
values_list = list(values)
b_value = values_list[4]

print(b_value)


# ------------------------------------------------------------------------------------




# ------------------------------------------------------------------------------------

def image_scrape(): # Could use url as a parameter...
    '''
    Scrape all hrefs of images for 1 item in a search result: 
    '''
    image_list = []

    for href in href_list:
    # Parse HTML and pull all href links
        response = requests.get(href_list[href])
        soup = BeautifulSoup(response.text, 'html.parser')

        image_grid = soup.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
        for i in image_grid:
            image_href = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
            image_list.append(image_href)
        return image_list
# print(image_scrape)



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
# print(category_type())


# ------------------------------------------------------------------------------------

