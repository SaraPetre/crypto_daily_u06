"""
Run the below script to create a database, named db_coins
and create a table named coins with the down below fields.
"""

import sqlite3


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


create_db()
