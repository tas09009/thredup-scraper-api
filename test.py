import requests, re
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
# import pandas as pd
# import timeit
# from href_list import href_list_1
# import sys
# from fake_useragent import UserAgent


url = 'https://www.thredup.com/product/women-cotton-forever-21-ivory-casual-dress/76517476'

response = requests.get(url)
product_page_soupified = BeautifulSoup(response.text, 'html.parser')

brand = []
brand_search = product_page_soupified.findAll('div', {'class': 'u-flex _20pksgdpcQ2E8r4MYcsBXl'})
for i in brand_search:
    product = i.find('a', {'class': '_32zNmjMSfxcoBWGGlzPobp'}).getText()
    brand.append(product)

print(brand)


# <div class="u-flex _20pksgdpcQ2E8r4MYcsBXl"><div><a class="_32zNmjMSfxcoBWGGlzPobp" 


# title="Forever 21" href="/women/forever-21?department_tags=women&amp;brand_name_tags=Forever%2021">Forever 21</a> <span class="_2gP239lLt_bs4iB60hEm85">Casual Dress</span></div><div class="_1xsIebREJUeQxUjKSqd6e9">Size S</div></div>


# <a class="_32zNmjMSfxcoBWGGlzPobp" title="Forever 21" href="/women/forever-21?department_tags=women&amp;brand_name_tags=Forever%2021">Forever 21</a>