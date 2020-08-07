# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

frequents = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


def crack():

    with open("ciphertext.txt") as f:
        text = f.read()

    count_store = {}

    for letter in text:
        if re.match('[A-Z]', letter):
            if letter in count_store:
                count_store[letter] += 1
            else:
                count_store[letter] = 1

    count_store_items = list(count_store.items())
    count_store_items.sort(key=lambda x: x[1], reverse=True)
    count_store_items = [item[0] for item in count_store_items]

    for i in range(len(count_store_items)):
        text = text.replace(count_store_items[i], frequents[i])

    print(count_store)
    print(count_store_items)
    print(frequents)
    # return text


print(crack())
