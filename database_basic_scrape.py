import requests, re
from bs4 import BeautifulSoup
import pandas as pd
from proxies_list import proxies_pool

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

url2 = 'https://www.thredup.com/petite?department_tags=petite&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799%2C778&include_petite=true&skip_equivalents=true&sort=newest_first&page='

url = 'https://www.thredup.com/petite/dresses?search_tags=women-dresses&department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C791%2C799%2C774&sort=newest_first&page=1'


added_at_end = '&page=2'

# Lists to store scraped data
hrefs = []
image = []
materials = []
size = [] # ['Size S '] removes the word 'petite' as well, not needed
measurements = [] # ['24" Length']
category_type = [] # Tops, bottoms
price = []
brand = []


proxies = proxies_pool()


# ------------------------------------------------------------------------------------
'''
Extract product link for each item on page
'''


product_list = []
for page_number in range(1,2): # Everytime range increases, items increase by 50. Ordered by "Newest first"
    url_page = ((url) + str(page_number))

    # Parse HTML and pull all href links
    response = requests.get(url_page, proxies=proxies)
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


hrefs = hrefs[0:3]
for link in hrefs:
    response = requests.get(link, proxies=proxies)
    product_page_soupified = BeautifulSoup(response.text, 'html.parser')


    product_type = []
    product_type_search = product_page_soupified.findAll('nav', {'class': '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'})
    for i in product_type_search:
        product = i.find('a', {'class': 'spot-grey-7 JdCj53-vTvU5pLpj6NlFo'}).getText()
        category_type.append(product)

# ------------------------------------------------------------------------------------
    # product_page_soupified = response.css(section._36TeFiFjuh5xlahzk4iZeQ)

    image_search = product_page_soupified.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
    for i in image_search:
        product = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
        image.append(product)


    product_materials = []
    materials_search = product_page_soupified.findAll('div', {'class': '_2SuzvN3bcsWRtNcNiSLMGq'})
    for i in materials_search:
        product = i.find('p')
        product_materials.append(product)

    item = str(product_materials[1])[3:-4]
    materials.append(item)


    product_item_measurement_size = []
    measurement_size_search = product_page_soupified.findAll('ul', {'class': 'list-disc'})
    for i in measurement_size_search:
        product = i.findAll('li')
        product_item_measurement_size.append(product)

    item = product_item_measurement_size[1]
    size.append(str(item[0])[4:-13])
    measurements.append(str(item[1])[4:-5])


    price_search = product_page_soupified.findAll('section', {'class': '_36TeFiFjuh5xlahzk4iZeQ'})
    for i in price_search:
        product_price = i.find('span', {'class': 'RFcwwL7_eda8sdWkyafAr'}).getText()
        price.append(product_price)


    # price_search = product_page_soupified.findAll('section', {'class': 'ui-container u-flex _36TeFiFjuh5xlahzk4iZeQ'})
    # for i in price_search:
    #     product_price = i.find('span', {'class': 'RFcwwL7_eda8sdWkyafAr spot-coral price'}).getText()
    #     price.append(product_price)
        


    brand_search = product_page_soupified.findAll('div', {'class': 'u-flex _20pksgdpcQ2E8r4MYcsBXl'})
    for i in brand_search:
        product = i.find('a', {'class': '_32zNmjMSfxcoBWGGlzPobp'}).get('title')
        brand.append(product)

    # Show progress of completed items    
    # print('Completed {i}/50 items'.format(i=i)



print(hrefs)
print(len(hrefs))
print(len(image))
print(len(materials))
print(len(size)) 
print(len(measurements))
print(len(category_type))
print(len(price))
print(len(brand))


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

basic_scrape.to_csv(r'/home/taniya/Projects/Thredup-database/basic_scrape_test_dresses.csv', index=False, header=True)

