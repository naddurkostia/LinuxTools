#!/usr/bin/env python3

from cgitb import text
import phonenumbers
from phonenumbers import geocoder
  
text = input('Enter phone number: ')
phone_number = phonenumbers.parse(text) 

print(geocoder.description_for_number(phone_number, 'en'))   