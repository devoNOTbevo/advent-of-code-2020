f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

# Part 1
valid = []
for line in lines:
    split_line = line.split(':')
    range_and_letter_split = split_line[0].split(" ")
    range_values = range_and_letter_split[0].split("-")
    min = int(range_values[0])
    max = int(range_values[1])
    letter = range_and_letter_split[1]
    string_to_search = split_line[1]
    occurrences = string_to_search.count(letter)
    if min <= occurrences <= max:
        valid.append(f"{line} => {occurrences}")

print(f"Part 1 = {len(valid)} valid passwords")

# Part 2