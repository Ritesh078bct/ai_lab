def sorted_list(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

list= [5, 4, 11, 13, 51]
print("Original list: ", list)
# list.sort()
# print("Sorted list: ", list)

sorted_list = sorted_list(list)
print("Sorted list: ", sorted_list)
