import smtplib
from httpcore import URL
import pandas as pd
from pyfiglet import Figlet
 # import sqlite3 module
import sqlite3


def mailhog():
    f = Figlet(font='slant')
    print(f.renderText('Its all about crypto now!'))
    URL_Figlet=(f.renderText("Its all about crypto now!"))
    # create database object to connect 
    # the database DB_coins.db
    conn = sqlite3.connect("DB_coins.db", isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM coins", conn)
    db_df.to_csv('database.csv', index=False)
    #db_df=db_df[1:]
    URL=db_df
    print(db_df.to_string())

    From_addr= "aras@test.test"
    to_addr ="test@to.to"
    Subject= "Dayly report_crypto!"


    msg=f"From: {From_addr}\r\nSubject: {Subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for the top10 crypto coins! \n\n {URL_Figlet}\n\n{URL}." 
    server=smtplib.SMTP("localhost:1025")
    server.sendmail( From_addr,to_addr, msg)
mailhog()