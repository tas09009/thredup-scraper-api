
# Kanban Board



## To Do

**Inputs from user**
- [ ] sys.argv:
	- [ ] url
	- [ ] # of pages
		- [ ] All pages: program needs to know how many pages the search has + 1 (to be able to scrape until the last page)
	- [ ] file name and location

**Efficiency**
- [ ] functionize everything in database_basic_scrape
- [ ] parse a smaller section of a product's page (`ui-container u-flex _36TeFiFjuh5xlahzk4iZeQ`) which contains all elements that I'm looking for (double check): measurements, size, materials, etc.
	- [ ] only issue is not being able to scrape category_type (not included above)
	- [ ] 6125 lines of code - parsing entire product_page over and over
	- [ ] 107 lines of code - parsing just the element above
- [ ] simplify CSS tags (remove double tags)
- [ ] use scrappy instead of bs4. Scrappy is better designed for multi-page parsing

**Automate**
- [ ] append all items for all pages to a *single* csv file
	- [ ] If not: merge csv files within category_type 
- [ ] verify category_type for each csv
- [ ] merge all csv files together -> ready for data analysis!

**Features**
- [ ] bug tracker
- [ ] logger
- [ ] speed up program and compare log files
- [ ] View/preview images
- [ ] requirements.txt file + conda environment
- [ ] python library to be used outside of this environment
- [ ] blog post write-up
- [ ] create a new conda environment to upload

**Data Science/Machine Learning**
- [ ] Extract additional features from the "Description" column
	- [ ] color, sleeve length, neckline, etc.
- [ ] ml model to recommend calling based on style: boho, classic, etc.

**thredup_fav: remove all "sold" items from favorites**

- [ ]  log into thredup
- [ ]  navigate to "favorites" page
- [ ]  automatically run script every 3 months?

**thredup_fibers: *sort by specific fabrics (Ex: 100% silk)**

- [ ]  Which one? See: "*How to sort" below*
    - [ ]  Search: "petite" word throughout "100% silk" dresses
    - [ ]  Search: "100% silk" word throughout "petite" dresses

---

## In Progress
**Autumn Wardrobe**
- [x] at least 300 items per category
	- [x] sweaters
	- [x] jacket
	- [x] long-sleeve shirt
	- [x] long-sleeve dress. Can be wool
	- [x] pants
- [ ] merge all tables together
	- [ ] category_type of sweaters is tops. Manual change

- [ ] create a kanban board on github :D

**Readme.md + github**
- [ ] Organize README.md
- [x] Clean up all code (as much as possible)
- [x] files -> directories


---


## Done
**Webscrape 1st edition**
- [x] basic database scrape - FINALLY DONE

**Avoid Blocks**
*Based on looking through the robots.txt file and realizing the need to buy premium proxies, will scrape as normal*
- [x] ~~learn how to use try/except for proxies_list. Except: use own IP address~~ 
	- *not worth the effort.*
- [x] ~~Rotate through a headers pool~~
	- *too complex for this project*

**Miscellaneous**
- [x] csv file
- [x] remove all urls except for the main one
- [x] Change name to 'Thredup API'
- [x] convert price to numbers. Right now it's a string
- [x] slow down scraping. Randomize requests between 10 - 20 seconds
- [x] print progress bar

**Readme.md + github**
- [x] send both to Github. Notes as README.md page
- [x] Approve "little_feature" + "basic_scrape" mergers, in that order

**Category labels**
- [x] Main clothing categories: dresses, tops, etc.
	- [x] Dictionary for categories within categories. Ex: dresses will have "Maxi" and "Midi" types where as tops will have "blouses" and "tunics"
		- [x] need a url for each category - regex urls 
			- [x] list of categories, for loop to use cateogry within a url

**Naming convention**
- [x] redo all variable names
	- [x] remove scrape at the end
- [x] remove variables with same name:
	- [x] Ex: product_item. Doesn't affect code. Just not good code I suppose

**advanced_webscrape**
*Description items to be divided *
- [x] category_scrape: list of clothing category titles (features)
	- [x] category_urls: url for each item in category_scrape
	- [x] product_filter_1sthalf: Product category type, first half of page
	- [x] pattern_accents_2ndhalf: Product category type, 2nd half of page	

**Product hrefs**
*scrape all items from search result*
- [x] pull href links for 1 search-result page
	- [x] combine with href header list: thredup.com
	- [x] for loop for multiple url pages
