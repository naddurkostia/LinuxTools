#!/usr/bin/env python3

import enquiries
from os import link
from numpy import number
import pytube
from cgitb import text
from distutils.log import info
from ipaddress import ip_address
import geocoder as geo
from cgitb import text
import phonenumbers
from phonenumbers import geocoder
import requests
import youtube_dl
from cgitb import text
from translate import Translator
import json
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

options = ['Crypto Price', 'YT video downloader', 'IP Checker', 'Country Code Checker', 'Youtube Audio Downloader', 'Language Translation', 'Calculator', 'Instagram Photo Downloader']
choice = enquiries.choose('Choose one of these options: ', options)

if options == 'Hello World':
    print('You chose Hello World')
elif options == 'Do Something 2':
    print('You chose Do Something 2')
elif options == 'Do Something 3':
    print('You chose Do Something 3')
else:
    if choice == 'YT video downloader':
        print('You chose Hello World')
        link = input("Enter the link: ")
        yt = pytube.YouTube(link)
        yt.streams.first().download()
        print("Downloaded!", link)

    elif choice == 'Crypto Price':
        # url = "https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/global/ticker/ETHUSD"

        # headers = {
        # 	"X-RapidAPI-Key": "b41fcdb10bmshc8214c075e394acp1a55eejsna61d047ecf39",
        # 	"X-RapidAPI-Host": "bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com"
        # }
        
        # response = requests.request("GET", url, headers=headers)
        
        # # Print only Ethernet price
        # print("ETH Price: " + str(response.json()['last'])) 

        # Defining Binance API URL
        key = "https://api.binance.com/api/v3/ticker/price?symbol="

        # Making list for multiple crypto's
        currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT", "ETHUSDT", "SOLUSDT", "TRXUSDT", "BNBUSDT"]
        j = 0

        # running loop to print all crypto prices
        for i in currencies:

            # completing API for request
            url = key+currencies[j]  
            data = requests.get(url)
            data = data.json()
            j = j+1
            print(f"{data['symbol']} price is {data['price']}")


    elif choice == 'IP Checker':

        ip_address = geo.ip('me')
        print(ip_address)

        text = input("Enter the text: ")
        ip = geo.ip(text)
        print(ip.city)

        print(ip.latlng)

        info = geo.google('Kyiv')
        print(info.geojson)
        print(info.osm)
        print(info.wkt)

    elif choice == 'Country Code Checker':
        text = input('Enter phone number: ')
        phone_number = phonenumbers.parse(text) 
        print(geocoder.description_for_number(phone_number, 'en'))  

    elif choice == 'Youtube Audio Downloader':
        def download_ytvid_as_mp3():
            video_url = input("Enter URL of youtube video: ")
            video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
            filename = f"{video_info['title']}.mp3"
            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filename,
            }

            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print("Download complete... {}".format(filename))
        download_ytvid_as_mp3()

    elif choice == 'Language Translation':
        text = input("Enter text to translate: ")

        lang = input("Enter language(Spanish, German, etc): ")

        translator= Translator(to_lang=lang)
        translation = translator.translate(text)
        print (translation)

    elif choice == 'Calculator':
        def calculate():

            first = int(input("Enter first number: "))
            second = int(input("Enter second number: "))
            operator = input("Enter operator: ")


            if operator == '+':
                # print('{} + {} = '.format(first, second))
                print(first + second)

            elif operator == '-':
                # print('{} - {} = '.format(first, second))
                print(first - second)

            elif operator == '*':
                # print('{} * {} = '.format(first, second))
                print(first * second)

            elif operator == '/':
                # print('{} / {} = '.format(first, second))
                print(first / second)

            calculate()

    elif choice == 'Instagram Photo Downloader':
        link = input("Enter Instagram Image URL: ")

        driver = webdriver.Chrome('chromedriver')

        driver.get(link)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        img = soup.find('img', class_='FFVAD')
        img_url = img['src']

        r = requests.get(img_url)

        with open("instagram"+str(time.time())+".png",'wb') as f: 
            f.write(r.content)

        print('success')





    


