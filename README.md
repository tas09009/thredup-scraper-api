
# Thredup Scraper API
Thredup Scraper API is a python based webscraper that uses beautiful soup to extract clothing information onto a csv file.

**Inputs**
- url of thredup
- number of pages to be scrapped 
- file name and location to save csv output

## How it works
Beautiful Soup pulls all product links from a search page (50 per page) and then parses each product link to pull the following information:*

Information to be extracted | Function | Example
|---------------------------|----------|--------|
Link | url of each item on a page | [Item_Link](https://www.thredup.com/product/women-cotton-tommy-hilfiger-blue-pullover-sweater/58862377?sizing_id=750,755,756,765,791,799,774)
Category Type | clothing type | Tops
Image_Link | front picture of item | [Picture_Link](https://cf-assets-thredup.thredup.com/assets/174145145/retina.jpg)
Description | distinct features | 'Crew neckline', 'Color blocked detail', 'Long sleeve', 'Blue'
Materials | fabric content and it's percentage | 100% Cotton
Size | item size | Size XS  
Measurement | measurements depend on item itself | 28" Chest, 22" Length
Price | price | 3.99
Brand | name brand | Tommy Hilfiger


Picture of what the database looks like (so far). *You can also look at the "datasets/test_runs" to see csv examples.*
![basic_scrape_table_image](media/thredup_table.png)


## Table of Contents

- [Background](#Background)
- [Installation](#Installation)
- [Usage](#Usage)
- [Road Map](#Road\ Map)
- [Additional Modules](#Additional\ Modules)



## Background

### Purpose
> Most clothing is environmentally damaging to the environment, even AFTER it's been bought. For example, washing polyester or any plastic-made clothing in the washing machine releases micro-plastics in the ocean. In addition, wearing non-natural fibers is less comfortable, less breathable, and falls apart quicker than stronger fabrics made of linen, wool, silk, etc. Of course, we are speaking in general terms. Microplastics and environmental damage also depend on the company, manufacturer, process of using materials (Ex: recycled polyester), quality, etc. 
**Used clothing > new clothing**
> - Less environmental damage
> - less waste ($billions of usable clothing is thrown away each year)
> - less shipping involved. New items are shipped from location to location to create the final product where as a used item is shipped once to a new owner
> - more available styles since vintage pieces are hard to buy new
> - many more benefits that you can read here:
> Medium Article: [Should You Buy Clothes Second Hand To Reduce Your Environmental Impact?](https://medium.com/@tabitha.whiting/should-you-buy-clothes-second-hand-to-reduce-your-environmental-impact-1ef1cabee982)
> Fast company: [ThredUp's new tool calculates the carbon footprint of your closet](https://www.fastcompany.com/90451694/whats-the-carbon-footprint-of-your-closet-this-handy-tool-will-tell-you)

### Future Goals
> Make it *as easy as possible* to buy second hand clothing

- Python library to include for scraping:
    - thredup
    - poshmark
    - ebay
    - heroine
	- etsy
	- ebay
	- The Real Real (luxury)
	- Vestiaire Collective (luxury)
    - local thrift stores *How to get them online?*
- expand to men's clothing. Ex: grailed
- include a WHY section
- If a company has a store (ex: amour vert, reformation, etc.) then try on their clothes and remember their sizes
- order an item or two from them, then buy the used version online
- clothing websites should have a "used section" that you can sell back to them" elieen fisher now has this

### Current issues when searching for items on thredup
- limited filters within the "petite" category such as
	- not able to search by fabrics
		-Ex:  linen/cotton combination
		- Ex: 100% wool
	- not able to filter out fabrics
		- Ex: no polyester
		- Ex: no polyester **or** acrylic
	
### Solution: 
- filter out clothing by fabrics (polyester, polyamide, etc.)
	- second layer of filter for rayon, nylon, etc.
- sort out clothing specifically by fabrics (wool, linen, etc.)



---



## Installation
Two ways to install, the first being the easiest

### Conda environment
1. Clone this project and run everything in the provided conda environment: 
`git clone https://github.com/tas09009/thredup-scraper-api.git`
`_____________________________`

### Manual
2. Install Python 3.0 or greater and the following modules:
- requests
- re
- time
- random
- beautifulsoup
- pandas
- numpy
- alive_progress



---



## Usage
*Due to testing the scraping component, some of the inputs are hardcoded for now. The code is inefficient at the moment and will need to go through several revisions. Here are the instructions to get it working:*

1. Fork this directory and then go into the /thredup-scraper-api/code/database_basic_scrape.py file to change the following variables. This is the main .py file where everything runs.
2. Open up thredup.com and search for a category type (Ex: sweaters) and filter out by size and any of the other features you are specifically looking for
3. Line 32: Copy the url link and replace variable `url_original`
4. Line 51: range represents page numbers. Leave as 1 but change the second number to how ever many pages you want to scrape. If there are only 5 pages, then put down (1,6) since it needs to include the 5th page.
5. Line 187: change the location and name of the csv file to be exported. The default location is set to `thredup-scraper-api/datasets/test_runs`
6. Run the code or run through the terminal:

- Linux/Mac: `python ~/thredup-scraper-api/code/database_basic_scrape.py`

- Windows:

### Things to know:
- This project doesn't use rotating proxies and HTTP headers due to time/money. Therefore, the code has a 5-10 second timer delay to each request being pulled.
- Scraping one page i.e. 50 items per page, will take 6 to 8 minutes. 

---


## Road Map
See the [Projects Board](https://github.com/tas09009/thredup-scraper-api/projects/1) for the latest status


## Additional Modules
*This project contains other libraries/python programs separate from the database project within the '/code/additional_modules' directory. They are:

**thredup_tabs.py**
*Scrapes a given number of items within a search page to filter out clothing by the following "Materials":*
- Polyester
- Acrylic
- Fabric details not available
- No Fabric Content
-	**How to use it**
	- input: url of current page
	- output: new chrome tabs open one by one only showing fabrics that don't contain any of the banned words. 3 second delay per tab


*More will be added*
