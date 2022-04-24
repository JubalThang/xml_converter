import requests 
from bs4 import BeautifulSoup
import re

url_link = input("Paste url : ")
# book_name = input("Enter the name of the book: ")
# book_number = input("Enter the number of the book: ")
chapter_count = input("How many chapters in this book?: ")

counter = 1

lo = re.search('\.html',url_link).group()

url_link = re.sub(f'{lo}',f'{counter}xxx{lo}',url_link)

# to = int(chapter_count) + 1

for index in range(int(chapter_count)):
    url_request = re.sub('\dxxx',f'{index+1}', url_link)
    url = requests.get(url_request)
   
    # parsing the html
    soup = BeautifulSoup(url.content, "html.parser")

    # getting the chapter 
    c = soup.find('div', class_='c')

    # select multiple classes that have the input clase names
    divs = soup.find_all(attrs={'class': ['p','q1','q2','m']})

    # remove unwanted tags
    for r in divs:
       for cf in r.find_all("span", class_='cf'):
           cf.extract()

    # writing start here
    # The code are from /document/code/FetchWebsite/dummy.py
    with open(f'bibleTemp.xml', encoding='utf-8', mode='a') as f:
        chapter = ""
        f.write(f'<CHAPTER cnumber="{c.get_text(strip=True)}">')
        for p in divs:
            if p.find_all(attrs={'class': ['v-num']}) == []:
                vers = p.find(attrs={'class': ['v']}).get_text(strip=True)
                # vers = re.sub('\n', '', vers)
                # f.write(vers)
                chapter += vers 
            else:
                vnums = p.find_all(attrs={'class': ['v-num']})
                vs = p.find_all(attrs={'class': ['v']})
                for index,vnum in enumerate(vnums):
                    vers = f'{vnum.get_text(strip=True)} {vs[index].get_text(strip=True)}'
                    v = re.search('\d+-\d+|\d+', vers).group()
                    vers = re.sub(f'{v}',f'</VERS> <VERS vnumber="{v}">',vers)
                    # f.write(f'{vers}')
                    chapter += vers
        chapter = re.sub('</VERS>', '', chapter, 1)
        f.write(chapter)
        f.write('</VERS></CHAPTER>')
print('filed saved!')
