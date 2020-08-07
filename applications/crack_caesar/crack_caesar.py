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
    lump_text = text.replace(' ', '')

    for letter in lump_text:
        if re.match('[A-Z]', letter):
            if letter in count_store:
                count_store[letter] += 1
            else:
                count_store[letter] = 1

    total_letters = 0
    for item in count_store.items():
        total_letters += item[1]

    freq_store = {}

    for key, value in count_store.items():
        freq_store[key] = round(value / total_letters * 100, 2)

    freq_store_items = list(freq_store.items())
    freq_store_items.sort(key=lambda x: x[1], reverse=True)
    freq_store_items = [item[0] for item in freq_store_items]

    result_text = text
    for i in range(len(freq_store_items)):
        result_text = result_text.replace(freq_store_items[i], frequents[i])

    print(freq_store)
    print(freq_store_items)
    print(frequents)
    # return result_text


print(crack())
