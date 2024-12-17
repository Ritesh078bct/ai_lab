

def character_frequency(sentence):
    frequency = {}
    for character in sentence:
        if character == ' ':
            continue
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1
    return frequency

print("enter a sentence")
sentence = input()
frequency = character_frequency(sentence)
print(frequency)