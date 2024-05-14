##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd
import random


birthday_data_frame = pd.read_csv('./birthdays.csv')
birthday_data = pd.DataFrame.to_dict(birthday_data_frame, orient='records')
now = dt.datetime.now()
current_date = dt.datetime(year=now.year,month=now.month,day=now.day)
# current_date = {"year":now.year,"month":now.month,"day":now.day}
for data in birthday_data:
    birf = dt.datetime(year=data.get('year'), month=data.get('month'), day=data.get('day'))
    if birf.month == current_date.month and birf.day == current_date.day:
        
        randnum = random.randint(1,3)
        
        file = f'./letter_templates/letter_{randnum}.txt'
        with open(file=file,mode='r') as letter_data:
            letter = letter_data.read()
            finished_letter = letter.replace('[NAME]', data.get('name'))
            print(finished_letter)
        
        with open('../Birthday Wisher (Day 32) start/email.txt', 'r') as email:
            var = email.readlines()
            
        my_email = list()
        for line in var:
            line = line.replace("\n", "")
            my_email.append(line)
            
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email[0], password=my_email[1])
            connection.sendmail(from_addr=my_email,
                                to_addrs="jagaw31633@godsigma.com",
                                msg=f"Subject:Happy Birthday {data.get('name')} \n\n{finished_letter}")
        print("email sent")


#     with open('quotes.txt', 'r') as quotes_data:
#         quotes = quotes_data.readlines()

#     quote = random.choice(quotes)
#     print(quote)

    # with open('./email.txt', 'r') as email:
    #     var = email.readlines()

    # my_email = list()
    # for line in var:
    #     line = line.replace("\n", "")
    #     my_email.append(line)

#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email[0], password=my_email[1])
#         connection.sendmail(from_addr=my_email,
#                             to_addrs="jagaw31633@godsigma.com",
#                             msg=f"Subject:Quote\n\n{quote}")
#     print("email sent")

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




