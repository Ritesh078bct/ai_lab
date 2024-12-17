def check_even(number):
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


print("enter the number")  
number = int(input())
check_even(number)


