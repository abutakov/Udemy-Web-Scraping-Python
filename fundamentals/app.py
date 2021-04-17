'''
    Date: April 17, 2021
    Agenda: 
        Today I'm gonna setup my dev environment - DONE
        Get familiar with tools - IN PROGRESS
        Get as far as a can in web-scraping course

'''
from lxml import etree

tree = etree.parse("fundamentals/src/web_page.html")
title_element = tree.find("body/ul/li")
list_items = tree.findall("/body/ul/li")

for li in list_items:
    a = li.find("a")
    if a is not None:
        print(f"{li.text.strip()} {a.text}")
    else:
        print(li.text)

# print(list_items)

# print(etree.tostring(tree))