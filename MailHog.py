import smtplib
from httpcore import URL
import pandas as pd
from pyfiglet import Figlet
 # import sqlite3 module
import sqlite3
from tabulate import tabulate

def mailhog():
    f = Figlet(font='slant')
    print(f.renderText('Its all about crypto now!'))
    URL_Figlet=(f.renderText("Its all about crypto now!"))
    # create database object to connect 
    # the database DB_coins.db
    conn = sqlite3.connect("DB_coins.db", isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name', symbol 'Symbol',price_USD 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update' FROM coins", conn)
    df=pd.DataFrame(db_df)
    pdtabulate= lambda df:tabulate(df,headers = 'keys', tablefmt = 'rst', showindex=False )
    URL=pdtabulate(df)
    print(pdtabulate(df))


    From_addr= "aras@test.test"
    to_addr ="test@to.to"
    Subject= "Dayly report_crypto!"


    msg=f"From: {From_addr}\r\nSubject: {Subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for the top10 crypto coins! \n\n {URL_Figlet}\n\n{URL}." 
    server=smtplib.SMTP("localhost:1025")
    server.sendmail( From_addr,to_addr, msg)
mailhog()