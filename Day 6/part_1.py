import re

time = []
distance = []
with open("input2.txt") as input:
    lines = input.readlines()
    time = re.findall(r'\d+', lines[0].split(":")[1])
    distance = re.findall(r'\d+', lines[1].split(":")[1])


win_ways = []
for i in range(len(time)):
    w = 0
    for t in range(int(time[i])+1):
        if int(t) * (int(time[i]) - int(t)) > int(distance[i]):
            w += 1
    win_ways.append(w)

tot = 1
for w in win_ways:
    tot *= w
print(tot)
