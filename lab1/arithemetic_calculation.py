def arithmetic_calculation(num1,num2):
    s = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    return (s,difference,product,quotient)

print("enter the first number")
num1 = int(input())
print("enter the second number")
num2 = int(input())
sum,difference,product,quotient=arithmetic_calculation(num1,num2)


print(sum,difference,product,quotient)

