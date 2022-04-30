"""
Selecting the wanted data from db and creates a csv-file
"""
# import sqlite3 module
import sqlite3
# import pandas, pd
import pandas as pd
from tabulate import tabulate

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Its all about crypto now'))


def select_from_db():
    """
    Select the wanted data from database
    """
    conn = sqlite3.connect("db_coins.db", isolation_level=None,
                           detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name' , symbol 'Symbol' , price_USD 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update'  FROM coins", conn)
    db_df.to_csv('database.csv', index=False)
    print(tabulate(db_df, headers='keys', tablefmt='rst', showindex=False))


select_from_db()
