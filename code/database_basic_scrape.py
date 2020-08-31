import requests, re, time, random, csv
from bs4 import BeautifulSoup
import pandas as pd
# from progressbar import ProgressBar
from alive_progress import alive_bar
from href_scrape import href_scrape



# from proxies_list import proxies_pool

# ------------------------------------------------------------------------------------

'''
Input: 
- url: searched items

Output:
- hrefs: links of all products on all pages (50 links/page) 
- soupified_list: beautiful soup object (parsed html) of each link within hrefs


Sizes being used in this program:
XXS, XS, SM
00, 0, 2
28, 29

Exclude One size
'''


# url needs to be sorted by newest first

url_original = 'https://www.thredup.com/petite/tops?search_tags=women-tops&department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C791%2C799%2C774&sort=price_low_high'

url = url_original + '&page='

'''
csv_file = open('basic_scrape_test4.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Link', 'Category_Type','Image_Link', 'Description', 'Materials', 'Size', 'Measurements', 'Price', 'Brand'])
'''

# ------------------------------------------------------------------------------------
'''
Extract product link for each item on page
'''

# pages_total = range(2,5)

product_list = []
for page_number in range(4,6): # Everytime range increases, items increase by 50. Ordered by "Newest first"
    url_page = ((url) + str(page_number))

    # Parse HTML and pull all href links
    response = requests.get(url_page)
    main_page_items = BeautifulSoup(response.text, 'html.parser')
    # main_page_items = response.css(div.grid)

    grid_products = main_page_items.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
    for i in grid_products:
        product = i.find('a', {'class': '_1di0il_2VkBBwWJz9eDxoJ'}).get('href')
        product_list.append(product)

# ------------------------------------------------------------------------------------
# Code below will need to be indented to accomodate multiple page searches

    url_front = 'https://www.thredup.com'
    for a in product_list:
        hrefs.append(url_front + a)
    # This marks the end of the page search. Page 2, etc. now begins


    # hrefs = hrefs[0:2]
    
    with alive_bar(len(hrefs)) as bar:
        href_scrape(hrefs) # scrape all 50 items

        bar()

    from href_scrape import category_type, image, description, materials, size, measurements, price, brand

    basic_scrape = pd.DataFrame({
        'Link': href_scrape,
        'Category_Type': category_type,
        'Image_Link': image,
        'Description': description,
        'Materials': materials,
        'Size': size,
        'Measurements': measurements,
        'Price': price,
        'Brand': brand})

    # df = pd.DataFrame.from_dict(basic_scrape)

    basic_scrape.to_csv(r'/home/taniya/Projects/thredup-scraper-api/datasets/test_runs/test{page_number}.csv'.format(page_number=page_number), index=False, header=True)