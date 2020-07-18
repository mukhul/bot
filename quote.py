import requests, json
import config
import websocket
import time
import main


def last_quote():

    main_QUOTE_URL = '{}/v1/last_quote/stocks/TSLA'.format(main.BASE_URL)
    r = requests.get(main_QUOTE_URL)
    print(r.content)


last_quote()    