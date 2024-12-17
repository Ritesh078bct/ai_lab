def check_prime(given_number):
    for num in range(1,given_number):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        
number=int(input("enter number:"))
check_prime(number)