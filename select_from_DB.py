# import sqlite3 module
import sqlite3
# import pandas, pd
import pandas as pd
from tabulate import tabulate

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Its all about crypto now'))


def select_from_DB():
    conn = sqlite3.connect("DB_coins.db", isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT name 'Name' , symbol 'Symbol' , price_USD 'Price(USD)', change_1h_percent '1h %', change_24h_percent '24h %', change_7d_percent '7 day %',last_updated 'Last update'  FROM coins", conn)
    db_df.to_csv('database.csv', index=False)
    #print(db_df.to_string())
    #db_df.index=pd.DataFrame.index= +1
    print(tabulate(db_df,headers = 'keys', tablefmt = 'rst', showindex=False ))
select_from_DB()

# from prettytable import from_csv
# with open ("database.csv", "r") as f:
#     table= from_csv(f)
# table.align ="r"
# #print (table)
