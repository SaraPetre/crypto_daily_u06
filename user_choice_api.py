"""This is the file to run for the user. It contains all the steps needed in this project. This is an application creating a database, adding table, inserting values from API,
and sending a report by MailHog.

"""
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Its all about crypto now'))


def meny():
    """
    The choice meny for the user.
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|              WELCOME to this crypto application a la aras!!!            |')
    print('|         1. Create a database in sqlite                                  |')
    print('|         2. Download data from API, CoinGecko into database              |')
    print('|         3. Select the wanted data, create a csv-file                    |')
    print('|         4. Send a Mail with crypto report of the top 10 crypto.         |')
    print('|         5. End this application!                                        |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


while True:
    meny()
    choice = int(input("Please enter the nr of your choice: "))

    if choice == 1:
        print("Create a database in sqlite")
        print()
        from create_db import create_db
        print("You have created a database with the name db_coins.db and a table named coins. Now move ahead to step 2.")
        print()

    if choice == 2:  # Create user
        print("Download data from API, CoinGecko into database")
        print()
        from download_to_db import download_to_db
        print("You have downloaded data. Great job! Now move ahead to step 3.")
        print()

    if choice == 3:  # Select the wanted data, create a csv-file
        print("This script selects the wanted data and creates a csv-file")
        print()
        from select_from_db import select_from_db
        print("Check this out! Do you find any bullish ocr bearish-behaviur? Time to by or sell? \n\n Want to get the report on mail. Pick choice nr 4 down below in the meny ;-)")
        print()

    if choice == 4:  # Get a mail with the results of the TOP 10 crypto
        print("This script sends an email, through MailHog, with the results of the TOP 10 crypto")
        print()
        from mailhog import mailhog
        print("\n\nThe abowe report have been sent! \n\nCheck out the MailHog mail for the report! You can click and follow the down below link to open the mail in your browser.")
        print("http://localhost:8025/")

    if choice == 5:  # End this application.
        print("\u001b[2J")
        print("The application have been shut down!\n\n\n")
        break
create_db()
download_to_db()
select_from_db()
mailhog()
