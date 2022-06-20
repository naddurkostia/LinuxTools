#!/usr/bin/env python3

import enquiries
from os import link
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

options = ['YT video downloader', 'IP Checker', 'Country Code Checker', 'ETH Price', 'Youtube Audio Downloader']
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
    elif choice == 'ETH Price':
        url = "https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/global/ticker/ETHUSD"

        headers = {
        	"X-RapidAPI-Key": "b41fcdb10bmshc8214c075e394acp1a55eejsna61d047ecf39",
        	"X-RapidAPI-Host": "bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com"
        }
        
        response = requests.request("GET", url, headers=headers)
        
        # Print only Ethernet price
        print("ETH Price: " + str(response.json()['last'])) 

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

    


