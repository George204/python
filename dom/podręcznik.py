import os
import requests
url = "https://flipbook.apps.gwo.pl/book/getImage/bookId:2909/pageNo:"

for i in range(1, 317, 1):
    print(i)
    dom = url+str(i)
    print(dom)
    page = requests.get(dom)
    print(page)
    filename = str(i) + ".jpg"
    print(filename)
    with open(f"./folder/{filename}","wb") as file:
        file.write(page.content)