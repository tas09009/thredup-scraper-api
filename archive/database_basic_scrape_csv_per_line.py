import requests, re, time, random, csv
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar



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

url_original = 'https://www.thredup.com/petite/dresses?search_tags=women-dresses&department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C791%2C799%2C774&sort=newest_first'
url = url_original + '&page='

url_front = 'https://www.thredup.com'

# Lists to store scraped data
hrefs = []
image = []
materials = []
size = [] # ['Size S '] removes the word 'petite' as well, not needed
measurements = [] # ['24" Length']
category_type = [] # Tops, bottoms
price = []
brand = []

pbar = ProgressBar()
# ------------------------------------------------------------------------------------
'''
Extract product link for each item on page
'''
csv_file = open('basic_scrape_test4.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Link', 'Image_Link', 'Category_Type', 'Materials', 'Size', 'Measurements', 'Price', 'Brand'])


product_list = []
for page_number in range(1,2): # Everytime range increases, items increase by 50. Ordered by "Newest first"
    url_page = ((url) + str(page_number))

    # Parse HTML and pull all href links
    response = requests.get(url_page)
    main_page_items = BeautifulSoup(response.text, 'html.parser')
    # main_page_items = response.css(div.grid)

    
    grid_products = main_page_items.findAll('div', {'class': 'uiUj-TxKXzmIOHZu6poxM grid-item'})
    for i in grid_products:
        product = i.find('a', {'class': '_1di0il_2VkBBwWJz9eDxoJ'}).get('href')
        
        hrefs = url_front + product
        product_list.append(hrefs)
        csv_writer.writerow([hrefs])
# ------------------------------------------------------------------------------------
# Code below will need to be indented to accomodate multiple page searches

    
    
    # product_list = product_list[0:2]
    # print(product_list)
    
    href_list = product_list[0:3]
    for a in pbar(href_list):
        # hrefs = url_front + product_list[a]
        # print(hrefs)
        # print(product_list[a])
        # print(product_list[a])

        # csv_writer.writerow([hrefs)
        # csv_writer.writerow([product_list)
    # This marks the end of the page search. Page 2, etc. now begins
        # print(product_list[a])
        # break

    # hrefs = hrefs[0:2]
    # for link in pbar(hrefs):
        response = requests.get(a)
        product_page_soupified_all = BeautifulSoup(response.text, 'html.parser')
        product_page_soupified = product_page_soupified_all.find('section', class_= '_36TeFiFjuh5xlahzk4iZeQ')

        product_type = []
        product_type_search = product_page_soupified.findAll('nav', {'class': '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'})
        for i in product_page_soupified_all:
            category_type = i.find('a', class_= 'JdCj53-vTvU5pLpj6NlFo')#.getText()
            # category_type.append(product)
            # csv_writer.writerow([category_type])
    
        image_search = product_page_soupified.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
        for i in image_search:
            image = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
            # image.append(product)
            # csv_writer.writerow([image])

        # product_materials = []
        materials_search = product_page_soupified.findAll('div', {'class': '_2SuzvN3bcsWRtNcNiSLMGq'})
        for i in materials_search:
            material_page = i.find('p')
            # product_materials.append(product)

            # print(type(product))
            materials = material_page[1]
            # materials = (str(material_page[1]))[3:-4]
            # materials.append(item)
            # csv_writer.writerow([materials])
        


        product_item_measurement_size = []
        measurement_size_search = product_page_soupified.findAll('ul', {'class': 'list-disc'})
        for i in measurement_size_search:
            product = i.findAll('li')
            product_item_measurement_size.append(product)

            item = product_item_measurement_size[1]
            # size.append(str(item[0])[4:-13])
            # measurements.append(str(item[1])[4:-5])
            size = str(item[0])[4:-13]
            measurements = str(item[1])[4:-5]

            # csv_writer.writerow([size])
            # csv_writer.writerow([measurements])

        price_search = product_page_soupified.findAll('section', {'class': '_36TeFiFjuh5xlahzk4iZeQ'})
        for i in price_search:
            product_price = i.find('span', {'class': 'RFcwwL7_eda8sdWkyafAr'}).getText()
            # product_price_int = int(product_price[1:])
            # price.append(float(product_price[1:]))
            price = float(product_price[1:])

            # csv_writer.writerow([price])


        brand_search = product_page_soupified.findAll('div', {'class': 'u-flex _20pksgdpcQ2E8r4MYcsBXl'})
        for i in brand_search:
            brand = i.find('a', {'class': '_32zNmjMSfxcoBWGGlzPobp'}).get('title')
            # brand.append(product)
            # csv_writer.writerow([brand])
            

        csv_writer.writerow([hrefs, category_type, image, materials, size, measurements, price, brand])
        
        time.sleep(random.randrange(5,10))
        # Show progress of completed items    
        # print('Completed {i}/50 items'.format(i=i)



# print(hrefs)
# print(len(hrefs))
# print(len(image))
# print(len(materials))
# print(len(size)) 
# print(len(measurements))
# print(len(category_type))
# print(len(price))
# print(len(brand))

'''
basic_scrape = pd.DataFrame({
     'Link': hrefs,
     'Image_Link': image,
     'Materials': materials,
     'Size': size,
     'Measurements': measurements,
     'Category_Type': category_type,
     'Price': price,
     'Brand': brand})

# df = pd.DataFrame.from_dict(basic_scrape)

basic_scrape.to_csv(r'/home/taniya/Projects/thredup_database_bs4/basic_scrape_test3.csv', index=False, header=True)
'''
