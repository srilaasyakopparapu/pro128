from bs4 import BeautifulSoup
import time 
import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("C:/Users/laasy/Downloads/chromedriver_win32")
browser.get(start_url)
scraped_data = []
def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table=soup.find("table",attrs={"class","wikitable"})
    table_body=bright_star_table.find("tbody")
    table_rows=table_body.find_all("tr")
    for row in table_rows:
        table_cols=row.find_all("td")
        templist=[]
        print(table_cols)
        for col_data in table_cols:
            data=col_data.text.strip()
            templist.append(data)
    scraped_data.append(templist)
scrape()

stars_data=[]
for i in range(0,len(scraped_data)):
    star_names=scraped_data[i][1]
    distance=scraped_data[i][3]
    mass=scraped_data[i][5]
    radius=scraped_data[i][6]
    lum=scraped_data[i][7]
    required_data=[star_names, distance, mass, radius, lum]
    stars_data.append(required_data)
    
headers=['Star_name','Distance','Mass','Radius','Luminosity']
star_df1=pd.DataFrame(stars_data,columns=headers)
star_df1.to_csv("scraped_data.csv", index=True, index_label="id")