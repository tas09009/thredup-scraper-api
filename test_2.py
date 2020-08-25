import requests 
from pprint import pprint


'''
try:
    f = open('list_of_links.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
'''



#Lets test what headers are sent by sending a request to HTTPBin
r = requests.get('https://www.thredup.com/petite?department_tags=petite&sizing_id=765%2C799%2C791%2C774%2C755%2C756%2C750%2C778&include_petite=true')
pprint(r.json())