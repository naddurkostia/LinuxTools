#!/usr/bin/python3

import requests

url = "https://bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com/indices/global/ticker/ETHUSD"
headers = {
	"X-RapidAPI-Key": "b41fcdb10bmshc8214c075e394acp1a55eejsna61d047ecf39",
	"X-RapidAPI-Host": "bitcoinaverage-global-ethereum-index-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

# Print only Ethernet price
print("ETH Price: " + str(response.json()['last'])) 