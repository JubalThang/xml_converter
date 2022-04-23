import requests 
from bs4 import BeautifulSoup
import re

url_link = input("Paste url :")
chapter_count = input("How many chapters in this book?: ")
fr = re.search('\d+', url_link).group()
to = int(chapter_count) + 1

# print(f'{fr} + {chapter_count}')
for index in range(int(fr), to):
    url_request = re.sub('\d+', f'{index}', url_link)
    url = requests.get(url_request)
   
    soup = BeautifulSoup(url.content, "html.parser")

    c = soup.find('div', class_='c')
    result = soup.find_all('div', class_='p')

    for r in result:
       for cf in r.find_all("span", class_='cf'):
           cf.extract()

    with open(f'bibleTemp.xml', encoding='utf-8', mode='a') as f:
        f.write(f'<CHAPTER cnumber="{c.get_text(strip=True)}">')
        for p in result:
            nums = p.find_all("span", class_='v-num')
            vs = p.find_all("span", class_='v')
            for index,num in enumerate(nums):
                vers = f'{num.get_text(strip=True)} {vs[index].get_text(strip=True)}</VERS>'
                v = re.search('\d+', vers).group()
                m = re.sub('\d+',f'<VERS vnumber="{v}">', vers)
                f.write(m)
        f.write('</CHAPTER>')
print('filed saved!')
