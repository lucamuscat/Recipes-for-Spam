from scraper import Scraper 
from random import randint
website_url = 'https://www.bbcgoodfood.com/recipes/collection/gordon-ramsay'
scraper = Scraper(website_url)
recipes = list(scraper.extract_recipes_from_links(scraper.extract_valid_links()))


