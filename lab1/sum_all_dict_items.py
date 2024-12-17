
print("Enter the dictionary items")
dictionary_items = {}
while True:
    item = input("Enter the item: ")
    if item == "":
        break
    value = int(input("Enter the value: "))
    dictionary_items[item] = value

# sum_of_all_items = sum(dictionary_items.values())
print(dictionary_items.values())
sum_of_all_items=0

for item_value in dictionary_items.values():
    sum_of_all_items += item_value

print("The sum of all items in the dictionary is: ", sum_of_all_items)