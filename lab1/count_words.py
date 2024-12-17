def count_words(sentence):
    count=0
    for char in sentence:
        if char == ' ':
            count+=1
        
    return count+1


sentence = input("enter sentence:\n")
print(f"count in {sentence} is {count_words(sentence)}")
# words = sentence.split()
# print(words)
# print(f"number of words in the sentence is {len(words)}")