import requests 
from pprint import pprint



try:
    f = open('list_of_links.txt')
    if f.name == 'list_of_links.txt':
        raise Exception
except FileNotFoundError as standard:
    print(standard)
except Exception as standard:
    print("Error, don't open")
else:
    print(f.read())
    f.close
finally:
    print('Executing Finally...')
