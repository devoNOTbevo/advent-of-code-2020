f = open("input.txt", "r")
lines = [line.strip() for line in f.readlines()]

def get_values_from_line(line):
    split_line = line.split(':')
    range_and_letter_split = split_line[0].split(" ")
    range_values = range_and_letter_split[0].split("-")
    first_number = int(range_values[0])
    second_number = int(range_values[1])
    letter_to_find = range_and_letter_split[1]
    string_to_search = split_line[1]
    number_of_occurrences = string_to_search.count(letter_to_find)
    return first_number, second_number, letter_to_find.strip(), string_to_search.strip(), number_of_occurrences


# Part 1
valid = []
for line in lines:
    first_number, second_number, letter_to_find, string_to_search, number_of_occurrences = get_values_from_line(line)
    if first_number <= number_of_occurrences <= second_number:
        valid.append(f"{line} => {number_of_occurrences}")

print(f"Part 1 = {len(valid)} valid passwords")

# Part 2
valid = []
for line in lines:
    first_number, second_number, letter_to_find, string_to_search, number_of_occurrences = get_values_from_line(line)
    occurrences_indexes = [i for i, cur_letter in enumerate(string_to_search) if cur_letter == letter_to_find]
    first_idx_matches = False
    second_idx_matches = False
    for idx in occurrences_indexes:
        new_idx = idx + 1
        if(new_idx == first_number):
            first_idx_matches = True
        if(new_idx == second_number):
            second_idx_matches = True
    if (first_idx_matches and not second_idx_matches) or (not first_idx_matches and second_idx_matches):
        valid.append([letter_to_find, string_to_search])

print(f"Part 2 = {len(valid)} valid passwords")