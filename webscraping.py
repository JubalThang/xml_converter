import requests 
from bs4 import BeautifulSoup
import re
import os 

url_link = input("Paste url : ")
book_name = input("Enter the name of the book: ")

# method to validate chapter_count 
def chapterCount(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("You have to type a number! try again..")
            continue
        else:
            return userInput

# method to validate abbr_name
def abbrName(message):
    while True:
        try:
            userInput = str(input(message))
        except ValueError:
            print("You have to type character! try again..")
            continue
        else:
            return userInput

abbr_name = abbrName("Enter short abbr for the book: ")
chapter_count = chapterCount("How many chapters in this book?: ")


lo = re.search('\.html',url_link).group()
# add 1 in the url in case the url already has 1xxx.html in the link
url_link = re.sub(f'{lo}',f'{1}xxx{lo}',url_link)

# create a folder for the book in current directory
directory = f'./tdm_simple/'
file_name = f'{book_name}.xml'
file_path = os.path.join(directory,file_name)

# check the folder is weather already exists 
if not os.path.exists(directory):
    os.mkdir(directory)

with open(file_path, encoding='utf-8', mode='a') as f:
    f.write(f'<BIBLEBOOK bnumber="" bname="{book_name}" bsname="{abbr_name}">')
    for index in range(int(chapter_count)):
        url_request = re.sub('\dxxx',f'{index+1}', url_link)
        url = requests.get(url_request)
        # parsing the html
        # soup = BeautifulSoup(url.content, "html.parser") this is slower =
        soup = BeautifulSoup(url.content, 'lxml')
        # getting the chapter 
        c = soup.find('div', class_='c')
        # select multiple classes that have the input clase names
        divs = soup.find_all(attrs={'class': ['p','q1','q2','s1','m']})
        # remove unwanted tags
        for r in divs:
            for cf in r.find_all("span", class_='cf'):
                cf.extract()
        search_text = r'\d+-\d+|\d+'
        ver = ""
        # writing start here
        print(f'{book_name}{index+1}.xml start writing .........')
    
        f.write('\n')
        f.write(f'\t\t<CHAPTER cnumber="{c.get_text(strip=True)}">')
        for p in divs:
           spans = p.find_all("span")
           for span in spans:
               for sentc in span:
                    verse = sentc.get_text(strip=True)
                    if re.search(f'{search_text}', verse):
                        ver_num = re.search(f'{search_text}', verse).group()
                        verse = re.sub(f'{search_text}',f'</VERS>\n\t\t\t<VERS vnumber="{ver_num}">', verse)
                        ver += verse
                    else: 
                        ver += f'{verse}'
        ver = re.sub('</VERS>', '', ver, 1)
        f.write(f'{ver}</VERS>\n\t\t</CHAPTER>')
    f.write('\n</BIBLEBOOK>')
f.close()
print("Done writing.")
print('file saved!!!')
