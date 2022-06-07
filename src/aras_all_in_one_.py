"""This is an application creating a database, adding table, inserting values from API,
and sending a report by MailHog.

"""
import sqlite3
from sqlite3 import Error
import smtplib
import requests
import pandas as pd
from pyfiglet import Figlet
from tabulate import tabulate


def create_connection():
    """ create a database connection to the SQLite database
        specified by aras_file
    :param aras_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("aras_file.db")
        return conn
    except Error as err:
        print(err)

    return conn


def create_table(conn, sql_create_coins_table):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c_c = conn.cursor()
        c_c.execute(sql_create_coins_table)
    except Error as err:
        print(err)


def main():
    """
    This is the main def.
    """
    conn = sqlite3.connect("aras_file.db")

    sql_create_coins_table = """CREATE TABLE IF NOT EXISTS coins (
                                    "name" text UNIQUE,
                                    "symbol" text UNIQUE,
                                    "price_usd" integer UNIQUE,
                                    "change_1h_percent" integer UNIQUE,
                                    "change_24h_percent" integer UNIQUE,
                                    "change_7d_percent" integer UNIQUE,
                                    "last_updated" integer UNIQUE
                                );"""

    # create a database connection
    conn = create_connection()

    # create tables
    if conn is not None:
        # create coin table
        create_table(conn, sql_create_coins_table)
        # run the download_to_db
        download_to_db()
        # run update_values
        update_values()
        # run mailhog
        mailhog()

    else:
        print("Error! cannot create the database connection.")


def download_to_db():
    """
    This function downloades data from API to database.
    """
    database = sqlite3.connect("aras_file.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()
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
    database.commit()
    database.close()


def update_values():
    """
    This function updates the valus in the table in the database.
    """
    database = sqlite3.connect("aras_file.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()

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


def mailhog():
    """
    This funktion sends an email with the report, a table, of the top 10 coins.
    """
    f_f = Figlet(font='slant')
    print(f_f.renderText('Its all about crypto now!'))
    url_figlet = (f_f.renderText("Its all about crypto now!"))
    # create database object to connect
    # the database DB_coins.db
    conn = sqlite3.connect("aras_file.db", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name', symbol 'Symbol',price_USD 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update' FROM coins", conn)
    df_create_table = pd.DataFrame(db_df)

    def pdtabulate(df_d):
        return tabulate(df_d, headers='keys', tablefmt='rst', showindex=False)
    url = pdtabulate(df_create_table)
    print(pdtabulate(df_create_table))

    from_addr = "aras@test.test"
    to_addr = "test@to.to"
    subject = "Daily report_crypto!"

    msg = f"From: {from_addr}\r\nSubject: {subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for the top10 crypto coins! \n\n {url_figlet}\n\n{url}."
    server = smtplib.SMTP("localhost:1025")
    server.sendmail(from_addr, to_addr, msg)


if __name__ == '__main__':
    main()
