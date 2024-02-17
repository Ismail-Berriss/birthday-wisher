import pandas
import random
import smtplib
import datetime as dt

my_email = "ismailberriss@gmail.com"
password = "*********"
birthdays = pandas.read_csv("birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]


def add_birthday(name, email, year, month, day):
    global birthdays
    new_birthday_dict = {"name": name, "email": email, "year": year, "month": month, "day": day}
    birthday_dict.append(new_birthday_dict)
    birthdays = pandas.DataFrame(birthday_dict)
    birthdays.to_csv("birthdays.csv", index=False)


# add_birthday("Ismail", "ismailberriss@gmail.com", "2002", "2", "17")
# add_birthday("Anass", "Anassoslash@gmail.com", "2003", "2", "11")

date_now = dt.datetime.now().date()
for birthday in birthday_dict:
    if date_now.month == birthday["month"] and date_now.day == birthday["day"]:
        random_letter = random.choice(letters)
        with open(random_letter, "r") as file:
            letter = file.read()
        birthday_letter = letter.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
            )
