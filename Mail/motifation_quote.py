import smtplib
import datetime as dt
import random


now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 2:
    my_emails = "b.korojo@gmail.com"
    my_passwords = "abcd1234()"

    with open("Mail/quotes.txt", mode="r")as quotes:
        quote_list = quotes.readlines()
        random_quote = random.choice(quote_list)

    with smtplib.SMTP("smtp.gmail.com") as connections:
        connections.starttls()
        connections.login(user=my_emails, password=my_passwords)
        connections.sendmail(from_addr=my_emails, to_addr="123@gmail.com",
                             msg=f"Subject:Hello\n\n This is the email body\n\n{random_quote}")
