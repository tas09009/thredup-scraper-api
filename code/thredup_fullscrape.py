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

# --------------------------------------------------
""" Define inputs """

url1 = input("url link: ")
pages = int(input("# of pages to scrape - 5 minutes/page: "))
file_name = input("name of file to save as - located in data folder: ")


# --------------------------------------------------
def main():
    '''
    Input: 
    - url: searched items

    Output:
    - hrefs: links of all products on all pages (50 links/page) 
    - soupified_list: beautiful soup object (parsed html) of each link within hrefs

    '''
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
        grid_products = main_page_items.findAll(
            'div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
        for i in grid_products:
            product = i.find('a', {
                'class': '_1di0il_2VkBBwWJz9eDxoJ'
            }).get('href')
            product_list.append(product)

        url_front = 'https://www.thredup.com'
        for a in product_list:
            hrefs.append(url_front + a)

            # Lists to store scraped data for each of the 50 items per page
            category_type = []
            image = []
            description = []
            materials = []
            size = []
            measurements = []
            price = []
            brand = []

        with alive_bar(len(hrefs)) as bar:
            for link in hrefs:

                response = requests.get(link)
                product_page_soupified = BeautifulSoup(response.text,
                                                       'html.parser')

                product_type = []
                product_type_search = product_page_soupified.findAll(
                    'nav', {
                        'class':
                        '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'
                    })
                for i in product_type_search:
                    product = i.find(
                        'a', {
                            'class': 'spot-grey-7 JdCj53-vTvU5pLpj6NlFo'
                        }).getText()
                    category_type.append(product)

                image_search = product_page_soupified.findAll(
                    'div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
                for i in image_search:
                    product = i.find('a', {
                        'class': '_17adkz6zswDjAoZ8PhDmPr'
                    }).get('href')
                    image.append(product)

                description_mini_list = []
                description_search = product_page_soupified.findAll(
                    'ul', {'class': 'aP-V0hf_LsLppqBVnK0PT'})
                for i in description_search:
                    description_list_all = i.findAll('li')
                    for i in description_list_all:
                        description_text = i.text
                        description_mini_list.append(description_text)
                description.append(description_mini_list)

                product_materials = []
                materials_search = product_page_soupified.findAll(
                    'div', {'class': '_2SuzvN3bcsWRtNcNiSLMGq'})
                for i in materials_search:
                    product = i.find('p')
                    product_materials.append(product)

                item = str(product_materials[1])[3:-4]
                materials.append(item)

                product_item_measurement_size = []
                measurement_size_search = product_page_soupified.findAll(
                    'ul', {'class': 'list-disc'})
                for i in measurement_size_search:
                    product = i.findAll('li')
                    product_item_measurement_size.append(product)

                item = product_item_measurement_size[1]
                size.append(str(item[0])[4:-13])
                measurements.append(str(item[1])[4:-5])

                price_search = product_page_soupified.findAll(
                    'section', {'class': '_36TeFiFjuh5xlahzk4iZeQ'})
                for i in price_search:
                    product_price = i.find('span', {
                        'class': 'RFcwwL7_eda8sdWkyafAr'
                    }).getText()
                    price.append(float(product_price[1:]))

                brand_search = product_page_soupified.findAll(
                    'div', {'class': 'u-flex _20pksgdpcQ2E8r4MYcsBXl'})
                for i in brand_search:
                    product = i.find('a', {
                        'class': '_32zNmjMSfxcoBWGGlzPobp'
                    }).get('title')
                    brand.append(product)

                time.sleep(random.randrange(5, 10))
                bar()

            basic_scrape = pd.DataFrame({
                'Link': hrefs,
                'Image_Link': image,
                'Category_Type': category_type,
                'Description': description,
                'Materials': materials,
                'Size': size,
                'Measurements': measurements,
                'Price': price,
                'Brand': brand
            })

            basic_scrape.to_csv(
                r'/home/taniya/Projects/thredup-scraper-api/datasets/test_runs/autumn_clothing/pants{page_number}.csv'
                .format(page_number=page_number),
                index=False,
                header=True)

    # Filter by Fabrics
    def filter():
        df = pd.read_csv(
            f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/merged_{file_name}.csv'
        )
        df_materials_banned = ~df.Materials.str.contains(
            "Polyester|Polyamide|Polyethylene|Acrylic|No Fabric Content")
        df_materials_banned_removed = df[df_materials_banned]
        df_materials_banned_removed.to_csv(
            f'/home/taniya/Projects/thredup-scraper-api/data/test_runs/clean_{file_name}.csv',
            index=False)


# --------------------------------------------------
if __name__ == '__main__':
    main()
