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
html = tree.getroot()

title_elements = html.cssselect("title")[0]
print(title_elements.text)

first_paragraph = html.cssselect("p")[0]
print(first_paragraph.text)

list_items = tree.findall("/body/ul/li")

# xpath testing
list_elements = html.cssselect("li")
for li in list_elements:
    # need to use dot before // (e.g. './/...'), otherwise duplicate will be generated
    a = li.cssselect('a')
    if len(a) == 0:
        print(li.text)
    else: 
        print(f"{li.text.strip()} {a[0].text}")





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