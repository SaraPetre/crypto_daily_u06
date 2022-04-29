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
    print('|         5. End this application!                                        |')
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
        #create_DB()
    if choice == 2: #Create user
        print("Download data from API, CoinGecko into database")
        print()
        from download_to_DB import download_to_DB
        #download_to_DB()
        print("You have downloaded data. Great job! Now move ahead to step 3.")
        print()

    if choice == 3: # Select the wanted data, create a csv-file
        print("This script selects the wanted data and creates a csv-file")
        print()
        from select_from_DB import select_from_DB
        # select_from_DB()
        print("Check this out! Do you find any bullish ocr bearish-behaviur? Time to by or sell? \n\n Want to get the report on mail. Pick choice nr 4 down below in the meny ;-)")
        print()
    if choice == 4: # Get a mail with the results of the TOP 10 crypto
        print("This script sends an email, through MailHog, with the results of the TOP 10 crypto")
        print()
        from MailHog import mailhog
        #mailhog()
        print("\n\nThe abowe report have been sent! \n\nCheck out the MailHog mail for the report! You can click and follow the down below link to open the mail in your browser.")
        print("http://localhost:8025/")
    if choice == 5: # End this application.
        print(u"\u001b[2J")
        print("The application have been shut down!\n\n\n")
        break