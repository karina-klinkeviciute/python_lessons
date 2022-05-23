sentence = "When you innovate, you create new industries that then boost your economy. And when you create new industries and that becomes part of your culture, your jobs can't go overseas because no one else has figured out how to do it yet."

# for letter in sentence:
#     print(letter)

# print(sentence[6])

# print(sentence[5:8])

# length = len(sentence)

# print(length)

words = sentence.split()

# for word in words:
#     print(word)
    
words.reverse()

# print(words)

reversed_sentence = " ".join(words)

print(reversed_sentence)

