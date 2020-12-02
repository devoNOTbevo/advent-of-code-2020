f = open("input.txt", "r")
lines = []
for line in f:
    lines.append(int(line.strip()))

lines_copy = lines.copy()
continue_iteration = True
for line in lines:
    if continue_iteration:
        for other_line in lines_copy:
            lineSum = line + other_line
            if lineSum == 2020:
                product = line * other_line
                print(product)
                continue_iteration = False
                break
