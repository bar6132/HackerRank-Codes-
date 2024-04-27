def arrange(sentence):
    sentence = sentence.replace('.', '')
    words = sentence.split()
    words = sorted(words, key=len)
    sentence = ' '.join(words)
    sentence = sentence[0].upper() + sentence[1:-1].lower() + sentence[-1] + '.'
    return sentence

sentence = 'The lines are printed in reverse order.'

# Function Call
result = arrange(sentence)

# Print the Result
print(result)
