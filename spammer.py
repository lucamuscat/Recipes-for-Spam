from scraper import extract_valid_links, extract_steps_from_recipes
website_url = 'https://www.bbcgoodfood.com/recipes/collection/gordon-ramsay'

recipes = extract_steps_from_recipes(extract_valid_links(url=website_url))
text_dump = open('recipe_dump.txt','w')
for i in recipes:
    print(i)

