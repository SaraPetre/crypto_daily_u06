"""
This script send an email through MailHog with a report of the Top 10 crypto. To be able to run this script the docker image of mailhog needs to be running.
Connect by using "docker compose -up -d" in the terminal.
"""
import sqlite3
import smtplib
import pandas as pd
from pyfiglet import Figlet
from tabulate import tabulate


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
    # pdtabulate = lambda df_d: tabulate(df_d, headers='keys', tablefmt='rst', showindex=False)
    url = pdtabulate(df_create_table)
    print(pdtabulate(df_create_table))

    from_addr = "aras@test.test"
    to_addr = "test@to.to"
    subject = "Dayly report_crypto!"

    msg = f"From: {from_addr}\r\nSubject: {subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for the top10 crypto coins! \n\n {url_figlet}\n\n{url}."
    server = smtplib.SMTP("localhost:1025")
    server.sendmail(from_addr, to_addr, msg)


mailhog()
