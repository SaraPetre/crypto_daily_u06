import smtplib

From_addr= "aras@test.test"
to_addr ="test@to.to"
Subject= "Dayly report_crypto!"



msg=f"From: {From_addr}\r\nSubject: {Subject}\r\nTo: {to_addr}\r\n\r\n This is a message from MailHog.py. \n Find down below the daily prices for Bitcoin and Etherium." 
server=smtplib.SMTP("localhost:1025")
server.sendmail( From_addr,to_addr, msg)
