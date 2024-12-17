from datetime import datetime 
class Person:
    def __init__(self, name,country, birthdate):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(birthdate,'%Y-%m-%d')
    def find_age(self):
        current_date=datetime.now()
        year=current_date.year-self.date_of_birth.year
        month=current_date.month-self.date_of_birth.month
        if month<0:
            year-=1
            month+=12
        days=current_date.day-self.date_of_birth.day
        if days<0:
            month-=1
            days+=30
            if month<0:
                year-=1
                month+=12
        return f"{year} years {month} months and {days} days"

    def __str__(self):
        return f"Name:{self.name}\nCountry:{self.country}\ndate_of_birth:{self.date_of_birth}\nAge:{self.find_age()}"

name=input("enter your name :\n")
country=input("enter country name you're living in :\n")
date_of_birth=input("enter date of birth in 'YY-MM-DD' format:\n")

p1=Person(name,country,date_of_birth)
print(p1)
# age=p1.age()

# now=datetime.now()
# # print(now.strftime('%Y-%m-%d'))

# given=datetime.strptime('2002-1-14','%Y-%m-%d')
# print(given)
# year=now.year-given.year

# # print(days/365-(days/365).fixed(0))
# print(year)