import json
import sqlite3
import uuid

def init_db():
    con = sqlite3.connect('streaming-markets.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Streaming
                (Id text, Symbol text, Interval text, Close real, High real, Low real, Timestamp integer)''')
    con.commit()
    con.close()

def log_db(message):
    parsed = json.loads(message)

    k = parsed["k"]

    id = str(uuid.uuid4().hex) #Creates something like: 2345234jhkj345234jhkjhk2345234jhkjhk
    symbol = k["s"]
    interval = k["i"]
    close = float(k["c"])
    high = float(k["h"])
    low = float(k["l"])
    time = int(k["t"])

    print("log:")
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
