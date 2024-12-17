def calc_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calc_factorial(number-1)
    
print("enter the number")
number = int(input())
print(f"factorial of {number} is {calc_factorial(number)}")



# factorial=1
# for i in range(1,number+1):
#     factorial = factorial * i

# print(f"factorial of {number} is {factorial}")