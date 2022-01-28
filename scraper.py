from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import pandas as pd
import requests 

bright_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(bright_url)
print(page)

soup = bs(page.text, 'html.parser')
star_table = soup.find('table')
temp = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)
names = []
distance = []
radius = []
mass = []
for i in range(1, len(temp)):
    names.append(temp[i][1])
    distance.append(temp[i][3])
    radius.append(temp[i][6])
    mass.append(temp[i][5])
df = pd.DataFrame(list(zip(names, distance, radius, mass)),
 columns = ['Proper name', 'Distance', 'Radius', 'Mass'])
print(df)
df.to_csv('bright_stars.csv')