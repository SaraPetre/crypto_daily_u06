# import sqlite3 module
import sqlite3
# import pandas, pd
import pandas as pd

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Its all about crypto now'))




##database= sqlite3.connect("DB_coins.db")
# create the cursor object
##cur = database.cursor()

# display the data in the table by 
# executing the cursor object
## cur.execute("SELECT * from coins")

# fetch all the data and prints it out
# print(cur.fetchall())

def select_from_DB():
    conn = sqlite3.connect("DB_coins.db", isolation_level=None,
                        detect_types=sqlite3.PARSE_COLNAMES)
    db_df = pd.read_sql_query("SELECT * FROM coins", conn)
    db_df.to_csv('database.csv', index=False)
    # print(db_df)
    #db_df=db_df[1:]
    print(db_df.to_string())

select_from_DB()

from prettytable import from_csv
with open ("database.csv", "r") as f:
    table= from_csv(f)
table.align ="l"
print (table)
