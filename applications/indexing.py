# return all ios students

records = [
    ("Scott", "iOS"),
    ("Nick", "iOS"),
    ("Ryan", "DS"),
    ("Shaun", "DS"),
    ("Cal", "DS"),
    ("Jean", "Web"),
    ("Natalia", "Web"),
    ("Jessica", "Web"),
    ("Jonathan", "Web"),
]

iOS = []

for record in records:
    if record[1] == 'iOS':
        iOS.append(record)


def build_index(records):
    indexed_records = {}

    for name, track in records:

        if track in indexed_records:
            indexed_records[track].append(name)

        else:
            indexed_records[track] = [name]
    return indexed_records


indexed_records = build_index(records)

print(indexed_records['Web'])
