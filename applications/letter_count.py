example_string = "The quick brown fox jumps over the lazy dog"

example_string = example_string.replace(' ', '')

letter_counts = {}

for letter in example_string:
    letter = letter.lower()

    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

print(letter_counts)

sorted_letter_counts = sorted(
    letter_counts.items(), key=lambda x: x[1], reverse=True)

for pair in sorted_letter_counts:
    print(pair[0])
