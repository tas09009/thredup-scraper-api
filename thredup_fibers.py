# OBJECTIVE
# Filter out "petite" clothing items by from a search results by material (Ex: '100% linen')

import requests, time, re, sys, webbrowser, pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = 'https://www.thredup.com/women/dresses?search_tags=women-dresses&department_tags=women&text=100%25%20linen&sizing_id=750%2C755%2C756%2C765%2C791%2C799&include_petite=true&skip_equivalents=true'

response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.content, "html.parser")
items_table = soup1.find_all("img")

# print(items_table)




for i in items_table: 
    print(i)



# # Retrieve the site's page. The 'with'(Python closure) is used here in order to automatically close the session when done
# with requests.Session() as res: # Do we need session - just use get? Maybe it's becuase it uses the "with"?
#     proxies_page = res.get(url)
    
# # Create a BeutifulSoup object and find the table element which consists of all proxies
# soup = BeautifulSoup(proxies_page.content, 'html.parser')
# proxies_table = soup.find(id='proxylisttable')

# # Go through all rows in the proxies table and store them in the right format (IP:port) in our proxies list
# proxies = []
# for row in proxies_table.tbody.find_all('tr'):
#     proxies.append('{}:{}'.format(row.find_all('td')[0].string, row.find_all('td')[1].string))
# return proxies


# # url = sys.argv[1]
# # print(url)
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser") # <class 'bs4.BeautifulSoup'> # print(soup.prettify()) # class 'str'

# # Find all href links that contain: "_1di0il_2VkBBwWJz9eDxoJ". This element represents each item on the page
# list_link_partial = [link['href'] for link in soup.findAll("a", {"class": "_1di0il_2VkBBwWJz9eDxoJ"})]

# # Add the front part of the webpage to make a full html link
# url_front = 'https://www.thredup.com'
# list_link = [url_front + a for a in list_link_partial]
# pprint(list_link)



# # Open new tab for each link in list_link unless it contains the "banned" words
# for i in range(4):


    # Parses new webpage to find Materials
# url1 = list_link[i]

# soup1 = BeautifulSoup('<div class="_138U7gqcrSxaloaCpyMPZg"> </div>', "html.parser")
# print(soup1)


    


# des_attr = soup1.find_all(re.compile("138U7gqcrSxaloaCpyMPZg"))
# print(des_attr)

# # Prints all the URLs found within a page’s <a> tags:
# for link in soup1.find_all('a'):
#     print(link.get('href'))
    
# # all the text from a page:
# print(soup1.get_text())


 


# des_attr_text = str(des_attr[0])
# print(des_attr_text)

# if (des_attr_text.find('Petite') != -1):
#     petite_items.append(url1)
#     print ('Petite')
    
    
# print(petite_items)





# # Narrowing down the space to the article in the page
# #(since there are many other irrelevant elements in the page)
# article = soup.find(class_="article-wrapper grid row")

# # Getting the keywords section 
# keyword_section = soup.find(class_="keywords-section")
# # Same as: soup.select("div.article-wrapper grid row div.keywords-section")

# # Getting a list of all keywords which are inserted into a keywords list in line 7.
# keywords_raw = keyword_section.find_all(class_="keyword")
# keyword_list = [word.get_text() for word in keywords_raw]
    

'''

<div class="_138U7gqcrSxaloaCpyMPZg">Size 2 Petite</div>

root > div > main > div > div.ui-container.large.u-flex._1RpLE3GlFuO-wKs_5eXfYG > div._26i9YH4mUjBNuyFPsg7e8h > div.u-position-relative > div:nth-child(3) > div:nth-child(4) > div:nth-child(4)



<div class="_138U7gqcrSxaloaCpyMPZg">Size 00 Petite</div>

root > div > main > div > div.ui-container.large.u-flex._1RpLE3GlFuO-wKs_5eXfYG > div._26i9YH4mUjBNuyFPsg7e8h > div.u-position-relative > div:nth-child(3) > div:nth-child(48) > div:nth-child(4)



<div class="_138U7gqcrSxaloaCpyMPZg">Size 2 Petite</div>

#root > div > main > div > div.ui-container.large.u-flex._1RpLE3GlFuO-wKs_5eXfYG > div._26i9YH4mUjBNuyFPsg7e8h > div.u-position-relative > div:nth-child(3) > div:nth-child(4) > div:nth-child(4)



'''