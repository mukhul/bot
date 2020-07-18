import requests
import json
import config
import websocket

def on_open(ws):
    print("opened")
    auth_data = {
    "action": "authenticate",
    "data": {
        "key_id": config.API_KEY,
        "secret_key": config.SECRET_KEY
        }
    }

    ws.send(json.dumps(auth_data))

    listen_message = {"action": "listen", "data": {"streams": ["Q.TSLA","Q.AAPL","Q.MSFT"]}}

    ws.send(json.dumps(listen_message))


def on_message(ws, message):
    print("recieved message")
    print(message)

def on_close(ws):
    print("connection closed")

socket = "wss://data.alpaca.markets/stream"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()