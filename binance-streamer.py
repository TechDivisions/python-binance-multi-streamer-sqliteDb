import sys
import websocket
import datetime
import db

def on_message(ws, message):
    print()
    print(str(datetime.datetime.now()) + ": ")
    db.log_db(message)

def on_error(ws, error):
    print(error) 

def on_close(close_msg):
    print("### closed ###" + close_msg)


def streamKline(symbol, interval):
    websocket.enableTrace(False)
    socket = f'wss://stream.binance.com:9443/ws/{symbol}@kline_{interval}'
    ws = websocket.WebSocketApp(socket,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()

db.init_db()

if __name__ == "__main__":
    symbol = sys.argv[1]
    interval = sys.argv[2]

    print("symbol: " + symbol)
    print("interval: " + interval)
    streamKline(symbol, interval)