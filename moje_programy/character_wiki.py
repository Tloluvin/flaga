import random
import wikipedia as wiki
wiki.set_lang("pl")

def character(name):
    page = wiki.search(name)
    character_page = wiki.page(page[0])
    # img = wiki.page(page[0]).images
    # content = character_page.content
    content = wiki.summary(name, sentences=6)
    
    return content

# name = 'Bruce Lee'
# print(character(name))