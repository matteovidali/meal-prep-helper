# Goal of this file:
# Accpet a URL to a recipe site
# parse it and print only the ingredients and directions
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup
from readability import Document

url = "https://cooking.nytimes.com/recipes/1018684-classic-tiramisu"

def get_text_from_url(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = lines
    # drop blank lines
    return [chunk for chunk in chunks if chunk]


def readability_get(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    doc = Document(response.text)
    with open("CHECK.html", 'w') as outfile:
        outfile.writelines(doc.summary())

    waste_tags = ['<div', '</div>', '<p><picture>', '</picture></p>',
                  '</svg>', '</iframe>', '<hr']
    
    infile = open('CHECK.html', 'r')
    outfile = open('No_Images.html', 'w+')
    
    for line in infile:

        put_line = True 

        for tag in waste_tags:
            if tag in line:
                print('\033[93m'+"CUT!! \n" + line + '\033[0m')
                put_line = False
                break

        if put_line:
            outfile.write(line)
            print(line)

    infile.close()
    outfile.close()

#   with open("CHECK.html", 'r') as infile:
#       for line in infile:
#           print(line)

def parse_text(text, get_ingredients=True, get_meathod=True, get_ime=True, get_yeild=True, get_nutrition=True):
    ingredients = []
    meathod = []
    time = 0
    yeild = 0
    nutrition = []
    in_ingredients = False
    in_meathod = False
    for line in text:
        if in_ingredients:
            ingredients.append(line)
        if line.lower() == "ingredients":
            in_ingredients = True
            print(line)

if __name__ == "__main__":
#
#   text = get_text_from_url(url)
#   for line in text:
#       print(line)
    readability_get('https://sallysbakingaddiction.com/chocolate-lava-cakes/')

