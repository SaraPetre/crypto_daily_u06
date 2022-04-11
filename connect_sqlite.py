
import requests, sqlite3


# @app.on.event("startup")
# def startup():
    #'''
    # Open database connection
    #'''    
database = sqlite3.connect("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map")
cur = database.cursor()
d = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/map")
d = d.json()
crypto_symbols = d["Symbol"]
for dr in crypto_symbols:
        name = dr["Name"]
        sql = 'INSERT INTO Drivers (name,number) VALUES(?,?)'
        val = (name)
        cur.execute(sql,val)
