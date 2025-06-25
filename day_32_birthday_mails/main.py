import smtplib, random
from datetime import datetime
MY_EMAIL="test00mail0000@gmail.com"
PASSWORD= "dlwy bvtk ocie ykwv"

#info about current date
now=datetime.now()
n_day=str(now.day)
if len(n_day)==1:
    n_day="0"+n_day
n_month=str(now.month)
if len(n_month)==1:
    n_month="0"+n_month

#checking if someone has birthday today
with open("birthdays.csv") as f:
    bd_dates=f.readlines()
for date in bd_dates:
    date=date.replace("\n","")
    date_list=date.split(',')
    if date_list[3]==n_month and date_list[4]==n_day:
        #preparing letter
        which_letter=random.randint(1,3)
        with open(f"letter_templates/letter_{which_letter}.txt") as f:
            letter=f.read()
            letter=letter.replace("[NAME]",date_list[0])
        #sending letter
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=date_list[1],
                                msg=f'Subject:Happy birthday!!!\n\n{letter}')



