import requests

def get_price():

    url = "https://financialmodelingprep.com/api/v3/quote-short/TSLA?apikey=12001f04edd1498dfd8120001110d155"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)

    responseJson = response.json()
    print(responseJson[0]["price"])

get_price()    
