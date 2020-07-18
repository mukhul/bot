import requests, json
import config
import websocket
import time


BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDER_URL = '{}/v2/orders'.format(BASE_URL)
CLOCK_URL = '{}/v2/clock'.format(BASE_URL)


def last_quote():

    last_quote_url = "{}/symbol=MSFT".format(QUOTE_URL)
    r = requests.get(last_quote_url, headers=config.HEADERS)
    print(r.content)

def create_order(symbol, qty, side, type, time_in_force):

    data={
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }

    r = requests.post(ORDER_URL, json=data, headers=config.HEADERS)
    return json.loads(r.content)


def trail_buy(symbol, qty, side, type, time_in_force):

    while True:
        t_end = time.time() + 60 * 345

        if (time.time() == t_end) or (time.time() > t_end):
            break
        
        price = last_quote()

        while time.time() < t_end:
            new_price = last_quote()

            if new_price < price:
                price = new_price
                break

            elif new_price > price:
                create_order(symbol, qty, side="buy", type="market", time_in_force="gtc")
                break

        time.sleep(0.55)    
                
def trail_sell(symbol, qty, side, type, time_in_force):

    t_end = time.time() + 60 * 345

    while True:

        price = last_quote()

        if (time.time() == t_end) or (time.time() > t_end):
            create_order(symbol, qty, side="sell", type="market", time_in_force="gtc")
            break

        while time.time() < t_end:
            
            if new_price > price:
                price = new_price
                break

            elif new_price < price:
                create_order(symbol, qty, side="sell", type="market", time_in_force="gtc")
                break

        time.sleep(0.55)
                
                







        

