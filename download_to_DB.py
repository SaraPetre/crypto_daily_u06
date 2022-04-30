"""
Run the script to download data from the cryptcoin-API "CoinGecko"
into the creatad data base "db_coins.db".
"""
import sqlite3
import requests


def download_to_db():
    """
    Funktion to download API to database.
    """
    database = sqlite3.connect("db_coins.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()
    print(data)

    for coin in data:
        name = coin["name"]
        symbol = coin["symbol"]
        price_usd = coin["current_price"]
        change_1h_percent = coin["price_change_percentage_1h_in_currency"]
        change_24h_percent = coin["price_change_percentage_24h_in_currency"]
        change_7d_percent = coin["price_change_percentage_7d_in_currency"]
        last_updated = coin["last_updated"]
        val = (name, symbol, price_usd, change_1h_percent, change_24h_percent, change_7d_percent, last_updated)
        data = cur.execute('''INSERT OR IGNORE INTO coins VALUES(?,?,?,?,?,?,?)''', (val))
        data = cur.fetchall()
        # commit and close the database
    database.commit()
    database.close()


download_to_db()


def update_values():
    """
    If there have been changes in the values the down below function will do an update.
    """
    database = sqlite3.connect("db_coins.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()
    print(data)

    for coin in data:
        name = coin["name"]
        symbol = coin["symbol"]
        price_usd = coin["current_price"]
        change_1h_percent = coin["price_change_percentage_1h_in_currency"]
        change_24h_percent = coin["price_change_percentage_24h_in_currency"]
        change_7d_percent = coin["price_change_percentage_7d_in_currency"]
        last_updated = coin["last_updated"]
        val = (name, symbol, price_usd, change_1h_percent, change_24h_percent, change_7d_percent, last_updated)
        data = cur.execute("""UPDATE OR IGNORE coins SET name=?, symbol=?, price_USD=?,change_1h_percent=?, change_24h_percent=?, change_7d_percent=?, last_updated=?""", (val))
        data = cur.fetchall()
    database.commit()
    database.close()


update_values()
