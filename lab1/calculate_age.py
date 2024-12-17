import datetime
class Person:
    def __init__(self, name,country, birthdate):
        self.name = name
        self.country = country
        self.date_of_birth = birthdate
    
    def age(self):
        current_datetime=datetime.datetime.now()
        current_year=current_datetime.year
        current_month=current_datetime.month
        current_day=current_datetime.day
        # print(type(current_year))
        date_of_birth=self.date_of_birth.split('/')
        # print(date_of_birth)
        year_of_birth=int(date_of_birth[0])
        # print(year_of_birth)
        month_of_birth=int(date_of_birth[1])
        # print(month_of_birth)
        day_of_birth=int(date_of_birth[2])
        # print(day_of_birth)

        age_year=current_year-year_of_birth

        age_month=current_month-month_of_birth
        if age_month<0:
            age_year-=1
            age_month=age_month+12

        age_day=current_day-day_of_birth
        if age_day<0:
            age_month-=1
            age_day=age_day+30
            if age_month<0:
                age_year-=1
                age_month=age_month+12
        return [age_year,age_month,age_day]


# # print(datetime.datetime.now().day)
# x=datetime.datetime(2002,1,14)
# print(x.strftime("%A"))
name=input("enter your name :\n")
country=input("enter country name you're living in :\n")
date_of_birth=input("enter date of birth in 'YY/MM/DD' format:\n")

ritesh=Person(name,country,date_of_birth)
x=ritesh.age()
print(x)



