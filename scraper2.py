
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# URLto Scrape Data
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# Get Page
page = requests.get(url)

# Parse Page
soup = bs(page.text,'html.parser')

# Get <table> with class = 'wikitable sortable'
star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)


temp_list= []

# IMP NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.
# Hence check the index number poperly for star_table[1]
# Currently, there are there 3 table with class = "class":"wikitable sortable" and "Field brown dwarfs" Table is the 2nd table
# Thus the index is 1
table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")