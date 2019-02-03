import os
import datetime

from time import time
from os.path import isfile
from requests_html import HTMLSession



class Scraper:
    
    def __init__(self,website_url):
        self.website_url = website_url
        self.dump_file_name = 'recipes_dump.txt'
        self.session = HTMLSession()
        
    def extract_valid_links(self):
        #Start a web session
        if isfile(self.dump_file_name):
            '''
            mtime = modification time
            check if more than a day has passed
            since the dump file has been modified
            '''
            dump_mtime = self.modification_date(self.dump_file_name)
            if time() - dump_mtime < datetime.timedelta(days=1).total_seconds()/100:
                return None

    # Returns every line from every recipe
    def extract_recipes_from_links(self,valid_links):
        # If valid_links is empty read from dump.
        if not valid_links:
            with open(self.dump_file_name,'r') as dump_file:
                dump = dump_file.readlines()
                for i in dump:
                    yield i.replace('\n', '')
        else:
            raw_recipe_list = list()
            for i in valid_links:
                request = self.session.get(i)
                # Name of class which the website uses to hold the desired content.
                if request.html.find('.method__list'):
                    raw_recipe = request.html.find('.method__list')[0].text
                    raw_recipe_list.append(raw_recipe)
                    recipe_list = raw_recipe.split('\n')
                    for j in recipe_list:
                        yield j
                self.dump_recipe(raw_recipe_list)

    def dump_recipe(self,raw_recipe_list):
        with open(self.dump_file_name,'w') as dump:
            for i in raw_recipe_list:
                for j in i.split('\n'):
                    dump.write(j)
                    
    def modification_date(self,path_to_file):
        file_info = os.stat(path_to_file)
        modification_time = file_info.st_mtime
        return modification_time
