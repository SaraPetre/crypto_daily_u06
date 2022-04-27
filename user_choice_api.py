# This is the file to run for the user. It contains all the steps needed in this project.
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('Its all about crypto now'))


  
def meny(): # Main steps
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('|              WELCOME to this crypto application a la aras!!!            |')
    print('|         1. Create a database in sqlite                                  |')
    print('|         2. Download data from API, CoinGecko into database              |')
    print('|         3. Select the wanted data, create a csv-file                    |')
    print('|         4. Send a Mail with crypto report of the top 10 crypto.         |')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# meny()

while True:
    meny()
    choice = int(input("Please enter the nr of your choice: "))

    
    if choice == 1: #Create user
        print("Create a database in sqlite")
        print()
        from create_DB import create_DB
        print("You have created a database with the name DB_coins.db and a table named coins. Now move ahead to step 2.")
        print()
        create_DB()
    if choice == 2: #Create user
        print("Download data from API, CoinGecko into database")
        print()
        from download_to_DB import download_to_DB
        download_to_DB()
        print("You have downloaded data. Great job! Now move ahead to step 3.")
        print()

    if choice == 3: # Select the wanted data, create a csv-file
        print("This script selects the wanted data and creates a csv-file")
        print()
        from select_from_DB import select_from_DB
        select_from_DB()
        print(".")
        print()