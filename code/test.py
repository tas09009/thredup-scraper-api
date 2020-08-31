import requests, re
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
import random



from alive_progress import alive_bar
from alive_progress import bouncing_spinner_factory
# items = range(1000000)                  # retrieve your set of items
# with alive_bar(len(items)) as bar:   # declare your expected total
#     for item in items:               # iterate as usual
#         # process each item
#         bar()                        # call after consuming one item
bouncing_spinner_factory(3,5)