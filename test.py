import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import timeit


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



a = range(10) 
b = [] 
for looping in a:     
    b.append(looping*2)
    print('Completed {i}/50 items'.format(i=looping))