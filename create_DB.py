# Run the below script to create a database, named DB_coins 
# and create a table named coins with the down below fields.
import sqlite3


def create_DB():
        database= sqlite3.connect("DB_coins.db")
        cur = database.cursor()

        # execute the script by creating the 
        # table named coins and insert the data
        cur.executescript("""CREATE TABLE IF NOT EXISTS "coins" (
                "name"  TEXT UNIQUE,
                "symbol"        TEXT UNIQUE,
                "price_USD" INTEGER,
                "change_1h_percent"       INTEGER UNIQUE,
                "change_24h_percent"      INTEGER UNIQUE,
                "change_7d_percent"       INTEGER UNIQUE,
                "last_updated"      INTEGER UNIQUE
        );""")
        # commit the database
        database.commit()
        database.close()
create_DB()
