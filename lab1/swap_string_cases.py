def swapped_string(input_string):
    swapped_string = ""
    for character in input_string:
        
        if character.islower():
            swapped_string += character.upper()
        else:
            swapped_string += character.lower()
    
    return swapped_string

input_string=input("Enter a string: ")
print(f"Swapped string is: {swapped_string(input_string)}")
# print(ord('c'))