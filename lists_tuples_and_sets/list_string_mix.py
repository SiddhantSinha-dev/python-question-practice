# List and String combination

'''sentence = input("Please enter a sentence: ").replace('.', ' ').split() #What about',' '?' '!' etc
longest_w = ''
collect_lw = []
for word in sentence:
    if len(longest_w) <= len(word): # what happens in case of a tie
        longest_w = word

collect_lw.append(longest_w)
sentence.remove(longest_w)

for word in sentence:
    if len(longest_w) == len(word):
        collect_lw.append(word)

print(f"The number of words are: {len(sentence)+1}")
print(f'The longest word is: {longest_w}')
print(f'The list of longest words with equal length is:{collect_lw}')'''

# Shorter Method

sentence = input("Please enter a sentence: ").replace('.', ' ').split()
print(sentence)

longest_words = []
max_len = 0

for word in sentence:
    if len(word) > max_len:
        max_len = len(word)
        longest_words = [word]
    elif len(word) == max_len:
        longest_words.append(word)

print(f"The number of words are: {len(sentence)}")
print(f'The longest word(s): {longest_words}')