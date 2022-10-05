from multiprocessing import connection
import smtplib
import datetime as dt

my_emails = "b.korojo@gmail.com"
my_passwords = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connections:
    connections.starttls()
    connections.login(user=my_emails, password=my_passwords)
    connections.sendmail(from_addr=my_emails, to_addr="123@gmail.com",
                         msg="Subject:Hello\n\n This is the email body")

now = dt.datetime.now()
print(now)
print(now.year)

date_of_birth = dt.datetime(year=1995, month=12, day=15)
