
import json
import requests

url = "https://v6.exchangerate-api.com/v6/4c7c987629a9daf434ac285c/latest/EUR"

payload = {}
headers = {
  'Authorization': 'Token 4c7c987629a9daf434ac285c'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

print(response.json()['conversion_rates']['RON'])
