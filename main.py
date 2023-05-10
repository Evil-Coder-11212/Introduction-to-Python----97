user_input = input("Enter a sentence / word: ")
i = 0
word_count = 0
for char in user_input:
    i += 1
    if (char == " "):
        word_count += 1

print("Your number of characters are: ", i)
print("Your number of words are: ", word_count+1)
