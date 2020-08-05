def clean_up(s):
    if s == "":
        return s

    s = s.lower()
    s = s.strip()
    s = s.replace('\n', ' ')
    s = s.replace('\r', ' ')
    s = s.replace('\t', ' ')

    ignored = r'":;,.-+=/\|[]{}()*^&'
    new_s = ""
    for c in s:
        if c not in ignored:
            new_s += c

    return new_s


def word_count(s):
    store = {}

    s = clean_up(s)

    if s == "":
        return store

    splitted = s.split(' ')

    for word in splitted:
        if word != "":
            if store.get(word) is None:
                store[word] = 1
            else:
                store[word] += 1

    return store


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
