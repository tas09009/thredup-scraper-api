import requests, re, time, random, csv
from bs4 import BeautifulSoup
import pandas as pd
from progressbar import ProgressBar
from database_basic_scrape import basic_scrape

basic_scrape.to_csv(r'/home/taniya/Projects/thredup_database_bs4/basic_scrape_tops.csv', index=False, header=True)