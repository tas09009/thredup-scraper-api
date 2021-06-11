import pandas as pd
# import numpy as np
import re
from glob import glob


# Merge sweaters
stock_files = sorted(glob('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_interim/sweaters*.csv'))

merged_sweaters = pd.concat((pd.read_csv(file).assign(filename = file)
    for file in stock_files), ignore_index = True)

merged_sweaters.replace(['Tops'], 'Sweaters', inplace=True)

# merged_sweaters.drop('filename', axis=1, inplace=True)

merged_sweaters.to_csv('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_processed/merged_sweaters.csv', index=False)


# Merge category items to each other
item_list = ['coats', 'dresses', 'pants', 'tops']
for i in item_list:
    stock_files = sorted(glob('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_interim/{category}*.csv'.format(category=i)))

    merged_items = pd.concat((pd.read_csv(file).assign(filename = file)
    for file in stock_files), ignore_index = True)

    # merged_items.drop('filename', axis=1, inplace=True)

    merged_items.to_csv('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_processed/merged_{category}.csv'.format(category=i), index=False)


# Merge all items
stock_files = sorted(glob('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_processed/*.csv'))

merged_items = pd.concat((pd.read_csv(file).assign(filename = file)
for file in stock_files), ignore_index = True)

merged_items.drop('filename', axis=1, inplace=True)

merged_items.to_csv('/home/taniya/Projects/thredup-scraper-api/data/autumn_clothing_processed/merged_items_total.csv', index=False)