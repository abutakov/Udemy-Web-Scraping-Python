'''
    Date: April 17, 2021
    Agenda: 
        Today I'm gonna setup my dev environment - DONE
        Get familiar with tools - IN PROGRESS
        Get as far as a can in web-scraping course

    Notes: 

'''
from lxml import etree

tree = etree.parse("fundamentals/src/web_page.html")

list_items = tree.findall("/body/ul/li")

# xpath testing
list_elements = tree.xpath("//li")
for li in list_elements:
    text = li.xpath("//text()")
    print(text)





# print(etree.tostring(li))

# Practice
# print(title_element)

# for li in list_items:
#     a = li.find("a")
#     if a is not None:
#         print(f"{li.text.strip()} {a.text}")
#     else:
#         print(li.text)

# print(list_items)

# print(etree.tostring(tree))