#!/usr/bin/env python3
"""
Author : taniya <https://github.com/tas09009>
Date   : 2020-10-12
Purpose: Thredup scrape
"""

import requests, re, time, random, argparse, os, sys, csv, glob
from bs4 import BeautifulSoup
import pandas as pd
from alive_progress import alive_bar
# from materials_filter import filter

# --------------------------------------------------
""" Define inputs """

url1 = input("url link: ")
pages = int(input("# of pages to scrape - 5 minutes/page: "))
file_name = input("name of file to save as - (specify location): ")

'''
Use this url as a sample to scrape 4 items:
https://www.thredup.com/petite?chars_sleeve_length=short%20sleeve&department_tags=petite&search_tags=women-tops%2Cwomen-tops-button-down-shirts&sizing_id=750%2C755%2C756%2C765&skip_equivalents=true&state=listed&color_names=tan
'''
# --------------------------------------------------
def main():
    """Webscrape only product links and materials"""

    url = url1 + '&page='

    product_list = []
    # Everytime range increases, items increase by 50.
    for page_number in range(1, pages + 1):
        url_page = ((url) + str(page_number))

        # Parse HTML and pull all href links
        response = requests.get(url_page)
        main_page_items = BeautifulSoup(response.text, 'html.parser')

        hrefs = []
        product_list = []
        grid_products = main_page_items.findAll('div', {'class': 'grid-item'})
        for i in grid_products:
            product = i.find('a', {
                'class': 'WCdF1-WeVI0oEKb0AIa4c'
            }).get('href')
            product_list.append(product)

        url_front = 'https://www.thredup.com'
        for a in product_list:
            hrefs.append(url_front + a)

        materials = []

        with alive_bar(len(hrefs)) as bar:
            for link in hrefs:

                response = requests.get(link)
                product_page_soupified = BeautifulSoup(response.text,
                                                       'html.parser')

                product_materials = []
                materials_search = product_page_soupified.findAll(
                    'div', {'class': '_2pmDWTgK3W9qnhtkNz7uFZ'})
                for i in materials_search:
                    product = i.find('p')
                    product_materials.append(product)

                item = str(product_materials[1])[3:-4]
                materials.append(item)

                time.sleep(random.randrange(5, 10))
                bar()

        basic_scrape = pd.DataFrame({'Link': hrefs, 'Materials': materials})

        basic_scrape.to_csv(
            f'~/{file_name}{page_number}.csv',
            index=False,
            header=True)


# /home/taniya/Projects/thredup-scraper-api/data/test_runs


    # # Merge
    # os.chdir('/home/taniya/Projects/thredup-scraper-api/data/test_runs')
    # all_filenames = [i for i in glob.glob(f'{file_name}*.csv')]

    # combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    # combined_csv.to_csv(f'merged_{file_name}.csv', index=False)

    # # Filter - different methods. user input maybe at this point?
    # # filter()


# --------------------------------------------------
if __name__ == '__main__':
    main()

    # parser = argparse.ArgumentParser(
    #     description='Thredup scrape',
    #     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('url',
    #                     metavar='url',
    #                     type=str,
    #                     help='starts with \'https://www.thredup.com\'',
    #                     default='https://www.thredup.com/women?brand_name_tags=People%20Tree&department_tags=women&state=listed&sizing_id=765%2C799%2C791%2C774%2C755%2C756%2C750%2C778&include_petite=true')

    # parser.add_argument('pages',
    #                     metavar='pages',
    #                     type=int,
    #                     help='Number of pages to scrape (50 items per page)',
    #                     default=2)

    # parser.add_argument('-f',
    #                     '--no_filter',
    #                     help='DON\'T Filter out fabrics',
    #                     default='Filter out the following: Polyester, Polyamide, Acrylic, Fabric Not Found, No Fabric Content',
    #                     action='store_false')

    # return parser.parse_args()
