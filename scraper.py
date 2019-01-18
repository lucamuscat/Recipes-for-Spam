from requests_html import HTMLSession

def extract_valid_links(url):
    #Start a web session
    session = HTMLSession()
    #Get the web page's html
    website_request = session.get(url)
    #all the links which can be found on the web page.
    website_sub_links = website_request.html.absolute_links
    #All the valid recipes happen to be in the recipes directory.
    #None of the valid recipes contained category or collection.
    valid_links = [x for x in website_sub_links
                   if 'recipes' in x and
                   'category' not in x and
                   'collection' not in x]
    return valid_links

def extract_steps_from_recipes(valid_links):
    sesh  = HTMLSession()
    for i in valid_links:
        request = sesh.get(i)
        #Name of class which website uses to hold content.
        if request.html.find('.method__list'):
            raw_recipe = request.html.find('.method__list')[0].text
            recipe_list = raw_recipe.split('\n')
            for j in recipe_list:
                yield j







