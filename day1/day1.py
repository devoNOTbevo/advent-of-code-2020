import itertools

f = open("input.txt", "r")
lines = [int(line.strip()) for line in f.readlines()]


def find2020(iterable, size):
    combos = itertools.combinations(iterable, size)
    for combo in combos:
        if sum(combo) == 2020:
            product = 1
            for num in combo:
                product *= num
            print(product)
            print(combo)


# Part 1
find2020(lines, 2)

# Part 2
find2020(lines, 3)
