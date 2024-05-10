import smtplib
import datetime as dt
import random



now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open('quotes.txt', 'r') as quotes_data:
        quotes = quotes_data.readlines()

    quote = random.choice(quotes)
    print(quote)

    with open('./email.txt', 'r') as email:
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
                            msg=f"Subject:Quote\n\n{quote}")
    print("email sent")

