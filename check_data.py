import sqlite3

con = sqlite3.connect('streaming-markets.db')
cur = con.cursor()
cmd = "select * from Streaming"
cur.execute(cmd)

rows = cur.fetchall()

for row in rows:
    print(row)

con.close()   