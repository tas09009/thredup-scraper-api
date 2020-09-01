import requests, re
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
import random


url_original = 'https://www.thredup.com/petite/outerwear?search_tags=women-outerwear&department_tags=petite&skip_equivalents=true&sizing_id=765%2C756%2C774&sort=price_low_high&page=1'
url = url_original[:-1] #+ '&page='

print(url)