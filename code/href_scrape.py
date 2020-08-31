import requests, re, time, random
from bs4 import BeautifulSoup

# Lists to store scraped data
hrefs = []
image = []
description = []
materials = []
size = [] # ['Size S '] removes the word 'petite' as well, not needed
measurements = [] # ['24" Length']
category_type = [] # Tops, bottoms
price = []
brand = []

def href_scrape(hrefs):
    '''
    Takes in an input of a list of hrefs. For each link in href, extract:

    category_type
    image
    description
    materials
    size
    measurements
    price
    brand

    Also added a 5-10 second delay per scrape.
    '''
    for link in hrefs:
        response = requests.get(link)
        product_page_soupified = BeautifulSoup(response.text, 'html.parser')


        # product_type = []
        product_type_search = product_page_soupified.findAll('nav', {'class': '_3p7XtL0LlyGSi8UgI6EU3j _12-L0I76mLCOu9b4N_SCPU'})
        for i in product_type_search:
            category_type_text = i.find('a', {'class': 'spot-grey-7 JdCj53-vTvU5pLpj6NlFo'}).getText()
            category_type.append(category_type_text)


        image_search = product_page_soupified.findAll('div', {'class': '_30o7eOhD-KenCXDTlPWxw'})
        for i in image_search:
            image_href = i.find('a', {'class': '_17adkz6zswDjAoZ8PhDmPr'}).get('href')
            image.append(image_href)

        description_mini_list = []
        description_search = product_page_soupified.findAll('ul', {'class': 'aP-V0hf_LsLppqBVnK0PT'})
        for i in description_search:
            description_list_all = i.findAll('li')
            for i in description_list_all:
                description_text = i.text
                description_mini_list.append(description_text)
        description.append(description_mini_list)


        product_materials = []
        materials_search = product_page_soupified.findAll('div', {'class': '_2SuzvN3bcsWRtNcNiSLMGq'})
        for i in materials_search:
            materials_text = i.find('p')
            product_materials.append(materials_text)

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
            # product_price_int = int(product_price[1:])
            price.append(float(product_price[1:]))


        brand_search = product_page_soupified.findAll('div', {'class': 'u-flex _20pksgdpcQ2E8r4MYcsBXl'})
        for i in brand_search:
            product = i.find('a', {'class': '_32zNmjMSfxcoBWGGlzPobp'}).get('title')
            brand.append(product)


        time.sleep(random.randrange(5,10))


        # incase want to write to cvs per row:
        # csv_writer.writerow([hrefs, category_type, image, description, materials, size, measurements, price, brand])