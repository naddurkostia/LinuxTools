#!/usr/bin/env python3

import json
import requests
  
key = "https://api.binance.com/api/v3/ticker/price?symbol="
  
# Making list for multiple crypto's
currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT", "ETHUSDT", "SOLUSDT", "TRXUSDT", "BNBUSDT"]
j = 0
  
for i in currencies:

    url = key+currencies[j]  
    data = requests.get(url)
    data = data.json()
    j = j+1
    print(f"{data['symbol']} price is {data['price']}")
