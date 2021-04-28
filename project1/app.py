import requests 

resp = requests.get(url="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
print(resp.headers)