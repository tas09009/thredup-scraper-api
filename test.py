import requests, re
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
# import pandas as pd
# import timeit
# from href_list import href_list_1
# import sys
# from fake_useragent import UserAgent

url = 'https://www.thredup.com/product/women-rayon-ann-taylor-loft-maroon-casual-dress/80298374?sizing_id=755,765,778,750,756,774,791,799'



# Main page items
regular = 'https://www.thredup.com/products/petite?department_tags=petite&sort=Recently%20Discounted'

incognito = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true&sort=newest_first'

incognito_search = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true'

incog_newest_first = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=755%2C765%2C778%2C750%2C756%2C774%2C791%2C799&skip_equivalents=true&sort=newest_first&page=1'


response = requests.get(url)
product_page_soupified = BeautifulSoup(response.text, 'html.parser')



price = []
price_search = product_page_soupified.findAll('div', {'class':'primary-info-row price-current-previous'})
for i in price_search:
    product_price = i.find('span', {'class': 'price'}).getText()
    price.append(product_price)
    print(product_price)
print(price)




'''
category_type = []
product_type_search = product_page_soupified.findAll('nav', {'class': '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'})
for i in product_type_search:
    product = i.find('a', {'class': 'spot-grey-7 JdCj53-vTvU5pLpj6NlFo'}).getText()
    category_type.append(product)
    print(product)
print(category_type)
'''