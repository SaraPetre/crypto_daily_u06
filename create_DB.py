# Run the below script to create a database, named DB_coins 
# and create a table named coins with the down below fields.
import sqlite3
database= sqlite3.connect("DB_coins.db")
cur = database.cursor()

# execute the script by creating the 
# table named coins and insert the data
cur.executescript("""CREATE TABLE IF NOT EXISTS "coins" (
        "id-coin"       INTEGER UNIQUE,
        "name"  TEXT UNIQUE,
        "symbol"        TEXT UNIQUE,
        "price" INTEGER UNIQUE,
        "price_percent_change_1h"       INTEGER UNIQUE,
        "price_percent_change_24h"      INTEGER UNIQUE,
        "price_percent_change_7d"       INTEGER UNIQUE
);""")
# commit the database
database.commit()
