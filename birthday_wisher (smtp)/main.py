import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL="kot.kiszon23@gmail.com"
PASSWORD='rejyvcyxoakshwsm'

birthday_man=''
birthday_man_email=''


def sending_email(text):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_man_email,
                            msg=f'Subject:Happy Birthday!!!\n\n{text}')

###getting  today's date
now=dt.datetime.now()
month=now.month
day=now.day

###checking has someone from the list got the birthday
bdays=pd.read_csv('birthdays.csv')

for(index,row) in bdays.iterrows():
    if row['month']==month and row['day']==day:
        birthday_man=row['name']
        birthday_man_email=row['email']
        ### picking random letter from the list
        random_letter=f'./letter_templates/letter_{random.randint(1,3)}.txt'
        with open(random_letter,'r') as file:
            wishes=file.read()
            wishes=wishes.replace('[NAME]',birthday_man)


sending_email(wishes)

















