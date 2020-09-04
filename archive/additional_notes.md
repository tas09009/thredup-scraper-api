
## Notes
*what percentage can be used for the following, after filtration indifferent to style. What about post style?*
Can I use ML to classify sweaters as actual sweaters?
- basically sort by fabrics first, then style, then price

### Description for tops:
- Search shorts: rompers are also displayed and identified as dresses
- contents of rayon, nylon and viscose cannot be higher than 50%
separate function that eliminates these materials completely

Style
shoulder cut - doesn't always pertain
pattern

accents
accents
accents
"work" - doesn't belong anywhere
neckline - contains the word neck
sleeve length - contains sleeve
color

## Website inconsistencies
- two tops are exactly the same but have different descriptions. [Here](https://www.thredup.com/product/women-cotton-ann-taylor-loft-pink-short-sleeve-blouse/79780008?sizing_id=750,755,756,765,774,778,791,799) and [here](https://www.thredup.com/product/women-cotton-ann-taylor-loft-red-short-sleeve-blouse/80488225?sizing_id=750,755,756,765,774,778,791,799)
	- this [blue top](https://www.thredup.com/product/women-rayon-ann-taylor-loft-outlet-teal-short-sleeve-blouse/80475452?sizing_id=750,755,756,765,774,778,791,799) and [white top](https://www.thredup.com/product/women-rayon-ann-taylor-loft-outlet-teal-short-sleeve-blouse/80475452?sizing_id=750,755,756,765,774,778,791,799) are similar to the red tops above. Again, different descriptions
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
- [ ] Integrate IP addresses [Web scraping with Python](https://medium.com/web-scraping-a-z) - 3 medium articles
- [ ] [robots.txt](https://www.thredup.com/robots.txt): rules of scraping such as frequency and specific pages
- [ ] Thredup doesn't have an API, not for Python atleast
- [robots.txt](https://www.thredup.com/robots.txt) doesn't seem to mind scraping petite items. No crawl rate mentioned either
- [ ] thredup should have a database of the top 10 brands and their measurements and it should automatically pull from that when a brand is matched


- [ ] where does Viscose fall into place?
- [ ] Some items sold are using 'recycled polyester' such as this [Eileen Fisher Trenchcoat](https://www.thredup.com/product/women-recycled-polyester-eileen-fisher-black-trenchcoat/80239531?sizing_id=750,755,756,765,774,791,799,778)
- [ ] how much of the clothing is fast fashion? obviously only in the petite category
- [ ] Other thredup projects:
	- [ ] [Thredup](https://github.com/sarc007/Thredup) A project to extract data from the website and do statistical calculations on it Below is the description of the requirement
	- [ ] [Thredup-Cart-Refresher](https://github.com/Eritz/Thredup-Cart-Refresher) Refreshes items inside the Thredup account's cart
	- [ ] [WebCrawler-ThredUp](https://github.com/yaisah/WebCrawler-ThredUp) I created this web crawler to scrape data from ThredUp products into a database
	- [ ] build a seasonal wardrobe with 5 items under $100 or $200? Use Vetta for ideas
## Learning
- git
- databases: postgresql + pgadmin
- documentation
- python fundamentals: functions, classes and data structures
- command line

## Fabrics
Sources:
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
		- Organized by **Newest First** which makes re-running code much easier, can update the database by webscarpping until first item is found already in the database	
- price - of course
- size - including petite site will already be filtered for petite items
- All item details
    - Description: dictionary with 6 to 8 keywords. These are values only. Need keys from search results link (left column). All values match a key to the columns on the left
    - Pull all keys from the columns first, then match their values based on the item description




# Python Script







# Issues & Ideas

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
Bad fabrics:
- polyester
- acrylic
- fabric not found, etc..
Good fabrics:
- cotton
- silk
- wool
- merino wool
- alpaca
- linen 
- hemp
- bamboo 
- tencel

## Lessons Learned
- Search by petite first, then sort. Rather than search all and then filter by petite. In the case of searching by a specific fabric (Ex: 100% merino wool), it's easier to search within the petite clothing and then filter out by fabric.
- difficult to loop through different clothing types **and** multiples pages within a clothing type. Easier for now to search for one clothing type at a time.


importing functions:  caused circular dependencies

- realized I cannot use Beautiful Soup HTML parser for Thredup because I cannot extract all the hrefs from the site for all the items. I have no idea where they are then! 
	- XML will be the way to go, all items are in a grid with the 2nd to last number increasing for each item.
- ~~add item per row, rather than at the end of the list~~ *would require too much memory and time to write each row rather than 50 rows at a time*



### Example of a garment bought on thredup vs new:

Links saved in Favorites for "loft romper"

---

---

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

# Thredup_Sort

Thredup is an online consignment store with thousands of options but their filtering system could be better. Due to environmental reasons, I only purchase clothing made of natural materials (wool, cotton, silk, etc.) and avoid polyester and any clothing where the fabric content is unknown.

The following code filters out clothing by removing search results with the words: "Polyester”, “Fabric details not available" and "No Fabric Content". A URL is input as a variable and all results (that don't contain the forbidden words) are opened in a new tab for viewing.


“url” – (line 11) the only input into the file. Take the current URL from the thredup page and replace the current default.


---
