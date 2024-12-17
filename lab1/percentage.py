def grade(percentage):
    if percentage>100:
        print("enter percentage between 0 to 100")
    elif percentage>=80:
        print("you passed with distinction")
    elif percentage>=65:
        print("you passed with first Division")
    elif percentage>=55:
        print("you passed with second Division")
    elif percentage>=40:
        print("you passed with third Division")
    else:
        print("you failed")

print("enter the percentage you got")
percentage= int(input())
grade(percentage)



