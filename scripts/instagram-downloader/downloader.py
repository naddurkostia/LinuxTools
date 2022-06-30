#!/usr/bin/env python3


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

link = input("Enter Instagram Image URL: ")

driver = webdriver.Chrome('chromedriver')

driver.get(link)

soup = BeautifulSoup(driver.page_source, 'lxml')

''' Extract the url of the image from the source code''' 
img = soup.find('img', class_='FFVAD')
img_url = img['src']


'''Download the image via the url using the requests library'''
r = requests.get(img_url)

with open("instagram"+str(time.time())+".png",'wb') as f: 
    f.write(r.content)

print('success')