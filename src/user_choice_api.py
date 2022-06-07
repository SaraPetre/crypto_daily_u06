"""This is the file to run for the user. It contains all the steps needed in this project. This is an application creating a database, adding table, inserting values from API,
and sending a report by MailHog.

"""
import sqlite3
import smtplib
import requests
import pandas as pd
from pyfiglet import Figlet
from tabulate import tabulate


def meny():
    """
    The choice meny for the user.
    """
    f_f = Figlet(font='slant')
    print(f_f.renderText('Its all about crypto now'))

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|                        WELCOME to this crypto application a la aras!!!                         |')
    print('|         1. Create a database in sqlite                                                         |')
    print('|         2. Download data from API, CoinGecko into database                                     |')
    print('|         3. Select the wanted data, create a csv-file                                           |')
    print('|         4. Send a Mail with crypto report of the top 10 crypto.                                |')
    print('|         5. Shortcut!! Create a database "aras_file.db" with everything above in one go!        |')
    print('|         6. End this application!                                                               |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def create_db():
    """
    Function to create the database and the table.
    """
    database = sqlite3.connect("db_coins.db")
    cur = database.cursor()

    # execute the script by creating the
    # table named coins in the database with the wanted varables.
    cur.execute("""CREATE TABLE IF NOT EXISTS "coins" (
                "name"  TEXT UNIQUE,
                "symbol"        TEXT UNIQUE,
                "price_usd" INTEGER,
                "change_1h_percent"       INTEGER UNIQUE,
                "change_24h_percent"      INTEGER UNIQUE,
                "change_7d_percent"       INTEGER UNIQUE,
                "last_updated"      INTEGER UNIQUE
        );""")
    # commit and close the database
    database.commit()
    database.close()


def download_to_db():
    """
    Funktion to download API to database.
    """
    database = sqlite3.connect("db_coins.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()
    #  print(data)

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


def update_values():
    """
    If there have been changes in the values the down below function will do an update.
    """
    database = sqlite3.connect("db_coins.db")
    cur = database.cursor()

    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d"

    data = requests.get(url)
    data = data.json()
    #  print(data)

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


def select_from_db():
    """
    Select the wanted data from database
    """
    conn = sqlite3.connect("db_coins.db", isolation_level=None,
                           detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name' , symbol 'Symbol' , price_USD 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update'  FROM coins", conn)
    db_df.to_csv('database.csv', index=False)
    print(tabulate(db_df, headers='keys', tablefmt='rst', showindex=False))


def mailhog():
    """
    This funktion sends an email with the report, a table, of the top 10 coins.
    """
    f_f = Figlet(font='slant')
    print(f_f.renderText('Its all about crypto now!'))
    url_figlet = (f_f.renderText("Its all about crypto now!"))
    # create database object to connect
    # the database db_coins.db
    conn = sqlite3.connect("db_coins.db", isolation_level=None, detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name', symbol 'Symbol',price_usd 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update' FROM coins", conn)
    df_create_table = pd.DataFrame(db_df)

    def pdtabulate(df_d):
        return tabulate(df_d, headers='keys', tablefmt='rst', showindex=False)
    url = pdtabulate(df_create_table)
    print(pdtabulate(df_create_table))

    from_addr = "aras@test.test"
    to_addr = "test@to.to"
    subject = "Dayly report_crypto!"

    msg = f"From: {from_addr}\r\nSubject: {subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for the top10 crypto coins! \n\n {url_figlet}\n\n{url}."
    server = smtplib.SMTP("localhost:1025")
    server.sendmail(from_addr, to_addr, msg)

print("\n\nStart creating your database with crypto info by going through the down below steps!")
while True:
    meny()
    choice = int(input("Please select the nr of your choice: "))

    if choice == 1:
        print()
        create_db()
        print("\u001b[2J")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nYou have created a database with the name db_coins.db and a table named coins. \n\nNow move ahead to step 2!")
        input("Press enter to continue to main menu!")
        print()

    if choice == 2:  # Create user
        print()
        download_to_db()
        update_values()
        print("\u001b[2J")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nYou have downloaded data from API, CoinGecko into database. Great job! \n\nNow move ahead to step 3, please!")
        input("Press enter to continue to main menu!")
        print()

    if choice == 3:  # Select the wanted data, create a csv-file
        print()
        print("\u001b[2J")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Check this table out! Do you find any bullish ocr bearish-behaviur? Time to buy or sell? \n\n Want to get the report on mail?\n Press enter and choose nr 4 down below in the meny ;-)\n\n")
        select_from_db()
        input()
        print()

    if choice == 4:  # Get a mail with the results of the TOP 10 crypto
        print("This script sends an email, through MailHog, with the results of the TOP 10 crypto")
        print()
        mailhog()
        print("\u001b[2J")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n\nThe report have been sent! \n\nCheck out the MailHog mail for the report! You can click and follow the down below link to open the mail in your browser.\n")
        print("http://localhost:8025/")
        input("\nPress enter to continue to main menu!")

    if choice == 5:  # Shortcut!! Create a database "aras_file.db" with everything above in one go!
        print("Shortcut!! Create a database 'aras_file.db' with everything above in one go!")
        print()
        from aras_all_in_one_ import create_connection, main
        create_connection()
        main()
        print("\u001b[2J")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("A database called 'aras_file.db' have been created. \nVisit SQlite in your browser or in your terminal. \nYou will also find a report sent to MailHog.")
        print("http://localhost:8025/")
        input("Press enter to continue to main menu!")

    if choice == 6:  # End this application.
        print("\u001b[2J")
        print("The application have been shut down!\n\n\n")
        break
