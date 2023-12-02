input = open("input.txt", "r")
sum = 0
for line in input.readlines():
    sum += int(''.join([[i for i in line if i.isdigit()][i] for i in (0, -1)]))
print(sum)
