# Basic product scrape
**basic_scrape.py**
*webscrapes individual product links from a search page (50 per page) and then parses each product link to pull the following information*

- product_href_scrape: urls of each item on a page
- image_scrape
- materials_scrape
- size
- measurement
- category_within_item

### To Do

Avoid getting blocked
- [ ] combine code with IP Addresses function (safeguard)
- [ ] or add 3 - 5 second delay per request

Naming convention
- [x] redo all variable names
	- [x] remove scrape at the end
- [x] remove variables with same name:
	- [x] Ex: product_item. Doesn't affect code. Just not good code I suppose

Track Time
- [ ] print time stamps for exports. progress bar?
- [ ] module: timeit - time each step of program. *tricky since everything is in a forloop*
	- [ ] send time outputs to a log file
	- [ ] speed up program and compare log files #Future
- [ ] progress bar of extracting the 30k+ items 

Readme.md + github
- [ ] Clean up all notes on this page
- [ ] Clean up all code (as much as possible)
- [ ] send both to Github. Notes as README.md page
- [ ] create a kanban board?
	- [ ] projects page?

### Done
- [x] ~~import files~~
	- [x] ~~soupified_list won't import at all: txt/py or str/non-string~~
- [x] csv file
- [x] remove all urls except for the main one









### Integrate IP addresses
- [ ] [Web scraping with Python](https://medium.com/web-scraping-a-z) - 3 medium articles



---

## Full product scrape
### Product hrefs
*scrape all items from search result*
- [x] pull href links for 1 search-result page
	- [x] combine with href header list: thredup.com
	- [x] for loop for multiple url pages

### Category labels
- [x] Main clothing categories: dresses, tops, etc.
	- [x] Dictionary for categories within categories. Ex: dresses will have "Maxi" and "Midi" types where as tops will have "blouses" and "tunics"
		- [x] need a url for each category - regex urls 
			- [x] list of categories, for loop to use cateogry within a url



### Putting it all together
*To be used later*
- category_scrape: list of clothing category titles (features)
	- category_urls: url for each item in category_scrape
	- product_filter_1sthalf: Product category type, first half of page
	- pattern_accents_2ndhalf: Product category type, 2nd half of page




- [ ] combine functions within each other *need to use classes*
	- [ ] watch video on [classes](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)
---
# Notes
- when jumping between different categories, the "sort by" method changes to "Recently Discounted" by default
- Only product filters all clothing items have in common are:
	- color
	- pattern
	- accents
- This project will be helpful to only those who are *petite* but eventually should expand to the others as well
	- Use [baserow](https://baserow.io/) as an online database to host the extension?
- Catch microplastics in wahsing machine (if you have to buy polyester) with: 
	- [coraball](https://coraball.com/)
	- [filtrol](https://filtrol.net/)
	- [Guppyfriend washing bag](https://us.guppyfriend.com/)
- [Express casual pants](https://www.thredup.com/product/women-polyester-express-maroon-casual-pants/78663501?sizing_id=750,755,756,765,774,791,799) - amour vert knockoff
- Thredup's classes, id, div tags all have unintuitive names. Other websites's labels make much more sense
- [thredup.com/robots.txt](https://www.thredup.com/robots.txt)
- Tutorial: [Web Scraping and BeautifulSoup](https://www.dataquest.io/blog/web-scraping-beautifulsoup/) exactly what I'm doing


## Clothing categories
*each type of clothing has it's own tags/features*
	*Ex:*
	
Occasion:
	casual
	formal
	work
	
Style:
	A-line
	Maxi
	Midi

### Regex for looping through all categories?
sorted by *newest first*

**All items:** 
/petite?department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&sort=newest_first&page=1

**Dresses:** *1st page*
/petite/ **dresses** ? **search_tags=women-dresses&** department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&sort=newest_first&page=1

**Dresses** *2nd page*
/petite **/dresses** ? **search_tags=women-dresses&** department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&sort=newest_first&page=2

**Tops** *Just do the whole thing:*
/petite **/tops?search_tags=women-tops&** department_tags=petite&include_petite=true&skip_equivalents=true&sizing_id=750%2C755%2C756%2C765%2C774%2C791%2C799&sort=newest_first&page=1

---


## Resources:
[Web scraping with Python — A to Z](https://towardsdatascience.com/web-scraping-with-python-a-to-copy-z-277a445d64c7) - follow this guide

[Automatic ticket classification](https://cdn2.hubspot.net/hubfs/307358/SmartAssist/E-books/SmartAssist_ThredUp_case_study.pdf) - thredup automated tickets 

---
## Questions to answer:
- what percentage of clothing is considered "environmentally damaging" i.e. made of "banned" products
- how many items are correctly sorted in their category?
	- Ex: clicked on casual dresses and many formal work dresses showed up
- how many items are missing categories such as "accents" and "pattern"
	- how many have a tag such as "3/4 sleeve" but don't belong to any category
	- **Use [[Machine Learning]] to fill in the gaps?**
- sizes vary per clothing item
	- Ex: size 00 and 0 for top but 2 for bottoms. But website cannot differentiate
- data may need to be cleaned up prior to putting into database?
	- links will need to be made beforehand
---

- item picture - high resolution only
- website link
	- very difficult to pull, none of the links would appear. Realized that the search results display in order of "Recently Discounted" with no account login. As opposed to how I was searching "Newest First" with account logged in
		- wow it's not even how it's sorted. It's the fact that there is no account logged in. Then it works??
		- Organized by **Newest First** which makes re-running code much easier, can update the database by webscarping until first item is found already in the database	
- price - of course
- size - including petite site will already be filtered for petite items
- All item details
    - Description: dictionary with 6 to 8 keywords. These are values only. Need keys from search results link (left column). All values match a key to the columns on the left
    - Pull all keys from the columns first, then match their values based on the item description

# [[Machine Learning]] in action:



# Python Script

### thredup_tabs: *sort by banned words (Ex: polyester)*

- [x]  get code to work with beta website
- [ ]  May need to log into thredup to do everything. First check with the API
- [ ]  all accepted clothing goes into a separate list instead
- [ ]  chrome to open all tabs within same browser - similar to OneTab
- [ ]  sys.argv to input url through command line

### thredup_fav: *remove all "sold" items from favorites*

- [ ]  log into thredup
- [ ]  navigate to "favorites" page
- [ ]  automatically run script every 3 months?

### thredup_fibers: *sort by specific fabrics (Ex: 100% silk)*

- [ ]  Which one? See: "*How to sort" below*
    - [ ]  Search: "petite" word throughout "100% silk" dresses
    - [ ]  Search: "100% silk" word throughout "petite" dresses

    ### Example #2: 100% linen tops

    - 1,285 - regular 26 pages
    - 1,323 - regular + petite 27 pages
    - difference: 39 items
    - When searching for 100% ____ items, use this method

    - 4,523 - petite tops - no fabric filter 91 pages
    - When searching for non-bad fabrics, use this method

# Issues & Ideas

- detailed email: all that is inconvenient + link to my thredup library. Would love to recommend the website to friends and others if these issues are fixed!
- sizing and fabrics are usually incorrect, which is problematic since my main filter is by fabric. I have returned a few items in the past but there were some I later saw the discrepancy and it was too late to return
- retail value incorrect. One blog mentioned this
- need more feedback loops from customers
- When I switch to Petite, all filters are reset
- Cannot search by material
- cannot search by eco-friendly materials either
- email: not recommendations (based on style and fabrics)
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
- PUZZLE POP UP? Wow this is amazing and perfect timing for me haha
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

### Quick Fix:

- remove items: polyester, acrylic, fabric not found, etc..
- new search criteria: 100% ________ cotton, silk, wool, merino wool, alpaca, linen, hemp, bamboo, tencel

### How to sort

- within search for regular clothing, sort by petite
    - URL for [100% silk tops](https://www.thredup.com/women/tops?search_tags=women-tops&department_tags=women&include_petite=true&sizing_id=755%2C765%2C750%2C756&text=100%25%20silk&skip_equivalents=true&page=5): 3,747 items
    - URL for [Petite tops](https://www.thredup.com/petite/tops?search_tags=women-tops&department_tags=petite&sizing_id=765%2C755%2C750%2C756&skip_equivalents=true): 4,531 items not necessarily a smaller amount
    - URL for [Petite tops, silk top (style)](https://www.thredup.com/petite/silk-tops?search_tags=women-tops%2Cwomen-tops-silk-tops&department_tags=petite&sizing_id=765%2C755%2C750%2C756&skip_equivalents=true): 146 items
- within petite clothing, search for 100% ______ (checkbox)

### Why to buy second-hand

Medium Article: [Should You Buy Clothes Second Hand To Reduce Your Environmental Impact?](https://medium.com/@tabitha.whiting/should-you-buy-clothes-second-hand-to-reduce-your-environmental-impact-1ef1cabee982)

Fast company: [ThredUp's new tool calculates the carbon footprint of your closet](https://www.fastcompany.com/90451694/whats-the-carbon-footprint-of-your-closet-this-handy-tool-will-tell-you)

### Example of a garment bought on thredup vs new:

Links saved in Favorites for "loft romper"

---
# Future

> End Goal: as *easy as possible* to buy second hand clothing

- Python library for second hand clothing to include:
    - thredup
    - poshmark
    - ebay
    - local thrift stores How to get them online?
- include a WHY section
- If a company has a store (ex: amour vert, reformation, etc.) then try on their clothes and remember their sizes
- order an item or two from them, then buy the used version online
- clothing websites should have a "used section" that you can sell back to them" elieen fisher now has this
