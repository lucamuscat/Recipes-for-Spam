from scraper import Scraper 
from random import randint
from pyperclip import copy
from pynput import keyboard
from pynput.keyboard import Key, Listener, KeyCode

website_url = 'https://www.bbcgoodfood.com/recipes/collection/gordon-ramsay'
scraper = Scraper(website_url)
recipes = list(scraper.extract_recipes_from_links(scraper.extract_valid_links()))


COMBINATION = {keyboard.Key.ctrl_l, keyboard.KeyCode(char='v')}
current = set()

def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            copy(recipes[randint(0,len(recipes)-1)])

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
