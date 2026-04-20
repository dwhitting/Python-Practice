import warnings
warnings.simplefilter("ignore")
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

data  = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

tables = soup.find_all('table')

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

print(tables[table_index].prettify())

"""
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

table = soup.find('table')

for row in table.find_all('tr'):
    cols = row.find_all('td')
    color_name = cols[2].string
    color_code = cols[3].string
    print("{}------>{}".format(color_name, color_code))

"""


"""
url = "https://web.archive.org/web/20230224123642/https://www.ibm.com/us-en/"
data = requests.get(url).text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a', href=True):
    print(link.get('href'))

print("\n\n\n")

for link in soup.find_all('img'):
    print(link)
    print(link.get('src'))

"""
"""
table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"

table_bs = BeautifulSoup(table, "html.parser")

table_rows = table_bs.find_all('tr')
first_row = table_rows[0]

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print('column', j, "cell", cell)

print("\n\n\n")

list_input = table_bs.find_all(name=["tr", "td"])
print(list_input)

print("\n\n\n")

print(table_bs.find_all(href=True))
"""


"""
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")

tag_object = soup.h3
#print("Tag o:", tag_object)
#print("of type:", type(tag_object))

tag_child = tag_object.b 
#print(tag_child)
parent_tag = tag_child.parent
#print(parent_tag)

sibling_1 = tag_object.next_sibling
#print(sibling_1)
sibling_2 = sibling_1.next_sibling
#print(sibling_2)
sibling_3 = sibling_2.next_sibling
#print(sibling_3)

temp = tag_child.attrs
#print(tag_child.get('id'))

tag_string = tag_child.string
print(tag_string)
print(type(tag_string))

unicode_string = str(tag_string)
print(unicode_string)
"""