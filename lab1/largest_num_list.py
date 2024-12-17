
def find_largest(num_list):
    largest_num = num_list[0]
    for num in num_list:
        if num > largest_num:
            largest_num = num
    return largest_num
num_list=[1,25,6,4,554,33,88,0]
print(f"The largest number in the list is: {find_largest(num_list)}")
