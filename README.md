
# Thredup Scraper API
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Thredup Scraper API is a command line, python based web scraper that uses beautiful soup to extract clothing information onto a csv file. Later the project will be migrated to a back end framework to use as an API.
## Table of Contents
- [How it works](#How-it-works)
- [Background](#Background)
- [Installation](#Installation)
- [Usage](#Usage)
- [Additional Web Scraping Scripts](#Additional-Web-Scraping-Scripts)
- [Contributing](#contributing)
- [License](#license)
- [Road Map](#Road-Map)

## Background
There are two ways to reduce your carbon footprint when it comes to clothing:
- buying used whenever possible
- consists of natural fabrics (wool, silk, cotton, etc.) over man-made fabrics 

This project is an attempt to combine the two ways by scraping for sustainable fabrics from the world's largest online consignment store. 

But clothing is environmentally damaging, even AFTER it's been purchased. For example, throwing polyester or any plastic-made clothing in the washing machine releases microplastics in the ocean. Of course, the environmental damage also depends on the company, manufacturer, process of using materials (Ex: recycled polyester), quality, etc. In addition, wearing non-natural fibers is less comfortable, less breathable, and falls apart quicker than stronger fabrics made of linen, wool, silk, etc.  

The basic rule to follow is **Used natural-fabric clothing > new clothing** for the following reasons:

- Less environmental damage
- less waste ($billions of usable clothing is thrown away each year)
- less shipping involved. New items are shipped from location to location to create the final product where as a used item is shipped once to a new owner
- more available styles since vintage pieces are hard to buy new
- many more benefits that you can read here: 
	- Medium Article: [Should You Buy Clothes Second Hand To Reduce Your Environmental Impact?](https://medium.com/@tabitha.whiting/should-you-buy-clothes-second-hand-to-reduce-your-environmental-impact-1ef1cabee982)
	- Fast company: [ThredUp's new tool calculates the carbon footprint of your closet](https://www.fastcompany.com/90451694/whats-the-carbon-footprint-of-your-closet-this-handy-tool-will-tell-you)

This program makes the following disctinctions between good vs. bad fabrics:

**Good fabrics:**
- cotton
- silk
- wool
- merino wool
- alpaca
- linen 
- hemp
- bamboo 
- tencel

**Bad fabrics:**
- polyester
- polyamide
- acrylic
- fabric not found*
- No Fabric Content*

*many items on the site don't have fabric information, so we will assume worst case scenario
## Installation
1. You can either clone the project by running`git clone https://github.com/tas09009/thredup-scraper-api.git` in your terminal or fork the project in order to contribute later: See [Contributing](#contributing) below.
2. Set up your Python virtual environment by running `pyvenv venv` in that directory and running `source venv/bin/activate` to active it. Or create a conda environment.
3. Install Python requirements with `pip install -r requirements.txt`.

## Usage
Run the program by typing `python code/thredup_fullscrape.py`. The terminal will then ask for the following three inputs: 
- url of thredup
- number of pages to be scrapped 
- file name and location to save csv output

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

Picture of what the data export. *You can also look at the "datasets/test_runs" to see more csv examples.*
![basic_scrape_table_image](media/thredup_table.png)

**FYIs:**
- This project does not use rotating proxies nor HTTP headers due to time/money. Therefore, the code has a 5-10 second timer delay to each request being pulled.
- Scraping one page i.e. 50 items per page, will take 6 to 8 minutes. 

## Additional Web Scraping Scripts
*This project contains other libraries/python programs separate from the database project within the '/code/additional_modules' directory. They are:*

### thredup_tabs.py
*Scrapes a given number of items within a search page to filter out clothing by the following "Materials":*
- Polyester
- Acrylic
- Fabric details not available
- No Fabric Content
All results (that don't contain the forbidden words) are opened in a new tab for viewing.

**Usage**
- input: url of current page
- output: new chrome tabs open one by one only showing fabrics that don't contain any of the banned words. 3 second delay per tab

### thredup_fav.py
*Removes all "sold" items from favorites list*

**Usage**
- input: url of "favorites" page
- output: CLI notifying when items have been removed. Refresh page to see updates.

*More to be added*
## Contributing
Please follow along this excellent [step-by-step guide](https://www.dataschool.io/how-to-contribute-on-github/) to learn how to contribute to an open-source project

## License

---
## Road Map
*The web scrapping code can be made more efficient such as scraping multiple elements from one CSS tag rather than the whole page. Right now, it's been built to work. The code will be updated at a later time. See the [Projects Board](https://github.com/tas09009/thredup-scraper-api/projects/1) for the latest status*

*The following sections include further research, plans, etc.*

## Table of Contents
- [Future Goals](#Future-Goals)
- [Questions to answer](#Questions-to-Answer)
- [Website inconsistencies](#Website-inconsistencies)
- [Lessons Learned](#Lessons-Learned)
- [Clothing Sustainabilty Issues & Ideas](#Clothing-Sustainabilty-Issues-&-Ideas)
- [Resources](#Resources)
### Future Goals
Make it **as easy as possible** to buy second hand clothing

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

## Questions to Answer:
- what percentage of clothing is considered "environmentally damaging" i.e. made of "banned" products
- how many items are correctly sorted in their category?
	- Ex: clicked on casual dresses and many formal work dresses showed up
- how many items are missing categories such as "accents" and "pattern"
	- how many have a tag such as "3/4 sleeve" but don't belong to any category
- sizes vary per clothing item
	- Ex: size 00 and 0 for top but 2 for bottoms. But website cannot differentiate
- data may need to be cleaned up prior to putting into database?
	- links will need to be made beforehand
- Machine Learning
	- Classify sweaters as actual sweaters?
	- Pick clothing based on fashion styles. Ex: boho, chic, grunge, etc.
- where does Viscose actually fall into place?
- Some items sold are using 'recycled polyester' such as this [Eileen Fisher Trenchcoat](https://www.thredup.com/product/women-recycled-polyester-eileen-fisher-black-trenchcoat/80239531?sizing_id=750,755,756,765,774,791,799,778)
- how much of the clothing is fast fashion? obviously only in the petite category
- Other thredup projects:
	- [Thredup](https://github.com/sarc007/Thredup) A project to extract data from the website and do statistical calculations on it Below is the description of the requirement
	- [Thredup-Cart-Refresher](https://github.com/Eritz/Thredup-Cart-Refresher) Refreshes items inside the Thredup account's cart
	- [WebCrawler-ThredUp](https://github.com/yaisah/WebCrawler-ThredUp) I created this web crawler to scrape data from ThredUp products into a database
	- build a seasonal wardrobe with 5 items under $100 or $200? Use Vetta for ideas
## Website inconsistencies
- limited filters within the "petite" category such as
	- not able to search by fabrics
		-Ex:  linen/cotton combination
		- Ex: 100% wool
	- not able to filter out fabrics
		- Ex: no polyester
		- Ex: no polyester **or** acrylic
- [shop by style](https://www.thredup.com/p/catalog/shop-by-style?tswc_redir=true) on thredup's website. All the links go to the same link for all womens clothing
- Search shorts: rompers are also displayed and identified as dresses
- two tops are exactly the same but have different descriptions. [Here](https://www.thredup.com/product/women-cotton-ann-taylor-loft-pink-short-sleeve-blouse/79780008?sizing_id=750,755,756,765,774,778,791,799) and [here](https://www.thredup.com/product/women-cotton-ann-taylor-loft-red-short-sleeve-blouse/80488225?sizing_id=750,755,756,765,774,778,791,799)
	- this [blue top](https://www.thredup.com/product/women-rayon-ann-taylor-loft-outlet-teal-short-sleeve-blouse/80475452?sizing_id=750,755,756,765,774,778,791,799) and [white top](https://www.thredup.com/product/women-rayon-ann-taylor-loft-outlet-teal-short-sleeve-blouse/80475452?sizing_id=750,755,756,765,774,778,791,799) are similar to the red tops above. Again, different descriptions
- when jumping between different categories, the "sort by" method changes to "Recently Discounted" by default
- Only product filters all clothing items have in common are:
	- color
	- pattern
	- accents
- This project will be helpful to only those who are *petite* but eventually should expand to the others as well
- Catch microplastics in washing machine (if you have to buy polyester) with: 
	- [coraball](https://coraball.com/)
	- [filtrol](https://filtrol.net/)
	- [Guppyfriend washing bag](https://us.guppyfriend.com/)
- [Express casual pants](https://www.thredup.com/product/women-polyester-express-maroon-casual-pants/78663501?sizing_id=750,755,756,765,774,791,799) - amour vert knockoff
- Thredup's classes, id, div tags all have unintuitive names. Other websites's labels make much more sense
- [thredup.com/robots.txt](https://www.thredup.com/robots.txt)
- Tutorial: [Web Scraping and BeautifulSoup](https://www.dataquest.io/blog/web-scraping-beautifulsoup/) exactly what I'm doing
- Integrate IP addresses [Web scraping with Python](https://medium.com/web-scraping-a-z) - 3 medium articles
- [robots.txt](https://www.thredup.com/robots.txt): rules of scraping such as frequency and specific pages
- Thredup doesn't have an API, not for Python atleast
- Thredup should have a database of the top 10 brands and their measurements and it should automatically pull from that when a brand is matched
- item picture - high resolution only
- website link
	- very difficult to pull, none of the links would appear. Realized that the search results display in order of "Recently Discounted" with no account login. As opposed to how I was searching "Newest First" with account logged in
		- Organized by **Newest First** which makes re-running code much easier, can update the database by webscarpping until first item is found already in the database	
- All item details
    - Description: dictionary with 6 to 8 keywords. These are values only. Need keys from search results link (left column). All values match a key to the columns on the left
    - Pull all keys from the columns first, then match their values based on the item description
## Lessons Learned
- Search by petite first, then sort. Rather than search all and then filter by petite. In the case of searching by a specific fabric (Ex: 100% merino wool), it's easier to search within the petite clothing and then filter out by fabric.
- difficult to loop through different clothing types **and** multiples pages within a clothing type. Easier for now to search for one clothing type at a time.
- filter out clothing by fabrics (polyester, polyamide, etc.)
	- second layer of filter for rayon, nylon, etc.
- sort out clothing specifically by fabrics (wool, linen, etc.)
- importing functions:  caused circular dependencies
- Can't use the Beautiful Soup HTML parser for Thredup because I cannot extract all the hrefs from the site for all the items. I have no idea where they are then! 
	- XML will be the way to go, all items are in a grid with the 2nd to last number increasing for each item.
- ~~add item per row, rather than at the end of the list~~ *would require too much memory and time to write each row rather than 50 rows at a time*

## Clothing Sustainabilty Issues & Ideas
- detailed email: all that is inconvenient + link to my thredup library. Would love to recommend the website to friends and others if these issues are fixed!
- sizing and fabrics are usually incorrect, which is problematic since my main filter is by fabric. I have returned a few items in the past but there were some I later saw the discrepancy and it was too late to return
- retail value incorrect. One blog mentioned this
- need more feedback loops from customers
- When I switch to Petite, all filters are reset
- Cannot search by material
- cannot search by eco-friendly materials either
- email: not recommendations based on style and fabrics
- Ask for access to API - read the docs
- read their engineering blog
- ML to create goody box
    - *don't like how I don't know what I'm getting*
    - display items within hours
    - choose what you like, or get similar recommendations
        - Suggested item: red turtleneck sweater. Suggested alternatives: different color, fabric, mockneck, etc.
- thredup monthly renting? similar to rent the runway? already do Goody Boxes and Rescues
    - How happy are people with the Goody Boxes and Rescues? Online research
        - Thredup must have this data in their yearly report?
    - *see ML info above*
    - ML to take monthly feedback to learn how to improve next time
        - better sizing
        - style (if people preferred blazers over sweaters
    - create a ML and test it (buy all the items as a "goody box" bundle
        - return and give feedback to ML model. Test again with another order
            - verify: sizing, color matching to original picture, fabric, original retail price estimation, cut accuracy
- [Blog post about using Goody Box](https://www.thefrugalfarmgirl.com/thredup-goody-box-review/). Send her two shipments and give some feedback to ML model?
- [Huge Rescue Mystery Box](https://www.youtube.com/watch?list=PLpyH557cISiwUBqZ78b7Jt7aQLN3WMD8o&time_continue=18&v=8dwDjKaodSA&feature=emb_title) prefers Free People. Preferences can be prioritized?
- competitor to Prime wardrobe but *better*
- possibility of adding men's clothing
- phase out bad fabrics. Over time when people donate and their items are logged into their accounts, a warning sign should come up saying we will not take polyester after this point
- get local thrift stores online as well. With thredup's help?
- Blog post: [11 ETHICAL OR SUSTAINABLE CLOTHING BRANDS LIKE EVERLANE](https://www.thredup.com/bg/p/brands-like-everlane?tswc_redir=true) is wildly inaccurate. write a comment on the site
    - Bad: Everlane, Madewell, Uniqulo: misrepresenting what "ethical" fashion mean. Goodonyou website proves this
        - Blog: [IS EVERLANE ETHICAL? WHY GOOD ON YOU’S RATING IS NOT QUITE ACCURATE](https://thegreenhubonline.com/2018/09/26/is-everlane-ethical-why-good-on-yous-rating-is-not-quite-accurate/) - oh crap. Who am I suppose to trust? This is getting exhausting
    - Good: Reformation
    - Don't know: *rest of the brands* Research
- Blog post: [6 MUST-WATCH DOCUMENTARIES TO LEARN ABOUT SUSTAINABLE FASHION](https://www.thredup.com/bg/p/6-must-watch-documentaries-to-learn-about-sustainable-fashion?tswc_redir=true). True cost mentions Uniqulo as "fast fashion" which it is. But in the blog above, it recommends it as ethical and sustainable clothing
- What are the best channels to reach out to Thredup?
- How trustable is good on you? Other websites that have more brand ratings? Tried out several on good on you and they didn't have it
- What if a local thrift store scanned the clothing tag, and it matched with the brand and page of the item with the picture?
- Build a database from web-scraping and save all important info:
    - picture
    - link to item
    - details: material
## Resources:
- [4 Fabrics That Are Harming Our Planet + What To Look For Instead](https://www.mindbodygreen.com/0-25104/the-4-most-toxic-fabrics-their-ecofriendly-upgrades.html)
- [The Most Harmful Fabrics in Fashion (and A Personal Challenge](https://www.jessannkirby.com/the-most-harmful-fabrics-in-fashion-and-a-personal-challenge/)
- banned fabric keywords: Polyester, Polyamide, Acrylic, No Fabric Content
- Next level to block: nylon, rayon, viscose
- Good fabrics: organic cotton, wool, silk, hemp, linen, cupro, ramie, tencel (used only)
- Iffy fabircs: 
	- modal 
		- Good: closed-loop system, fewer harmful byproducts 
		- Bad: semi-seynthetic
	- tencel
		- Good: closed-loop process. Depending on chemicals - biodegradable
		- Bad: man-made fabric. Heavy use of chemicals
	- Acetate and triacetate
		- Good: wood pulp
		- Bad: man-made fibre
- [Web scraping with Python — A to Z](https://towardsdatascience.com/web-scraping-with-python-a-to-copy-z-277a445d64c7) 
- [Automatic ticket classification](https://cdn2.hubspot.net/hubfs/307358/SmartAssist/E-books/SmartAssist_ThredUp_case_study.pdf) - thredup automated tickets 
- [robots.txt](https://www.thredup.com/robots.txt) doesn't seem to mind scraping petite items. No crawl rate mentioned either
- Use [baserow](https://baserow.io/) as an online database to host the extension?