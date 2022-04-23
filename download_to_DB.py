# Run the script to download data from the cryptcoin-API "CoinGecko"
# into the creatad data base "DB_coins.db".
import requests, sqlite3
database = sqlite3.connect("DB_coins.db")
cur = database.cursor()

url= "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=2&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

data = requests.get(url)
data = data.json()
print(data)

for c in data:
        id_coin = c["id"]
        name = c["name"]
        symbol=c["symbol"]
        price=c["current_price"]
        price_percent_change_1h = c["price_change_percentage_1h_in_currency"]
        price_percent_change_24h=c["price_change_percentage_24h_in_currency"]
        price_percent_change_7d=c["price_change_percentage_7d_in_currency"]

        val = (id_coin, name, symbol,price, price_percent_change_1h, price_percent_change_24h, price_percent_change_7d)
        cur.execute('''INSERT OR IGNORE INTO coins VALUES(?,?,?,?,?,?,?)''',val)
database.commit()