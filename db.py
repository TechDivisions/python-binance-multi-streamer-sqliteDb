import json
import sqlite3
import uuid

def init_db():
    con = sqlite3.connect('streaming-markets.db')
    cur = con.cursor()

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS Streaming
                (Id text, Symbol text, Interval text, Close real, High real, Low real, Timestamp integer)''')
    con.commit()

def log_db(message):
    parsed = json.loads(message)

    k = parsed["k"]

    id = str(uuid.uuid4().hex) #2345234jh-kjhk23-45234-jhkjhk-2345234jhkjhk
    symbol = k["s"]
    interval = k["i"]
    close = float(k["c"])
    high = float(k["h"])
    low = float(k["l"])
    time = int(k["t"])

    print("log:")
    # print(id)
    print("symbol: " + symbol)
    print("interval: " + interval)
    print("close: " + str(close))
    print("high: " + str(high))
    print("low: " + str(low))
    print("time: " + str(time))

    row = (id, symbol, interval, close, high, low, time)
    con = sqlite3.connect('streaming-markets.db')
    cur = con.cursor()
    cmd = "insert into Streaming (Id, Symbol, Interval, Close, High, Low, Timestamp) values (?, ?, ?, ?, ?, ?, ?)" 
    cur.execute(cmd, row)
    
    con.commit()
    con.close()    
