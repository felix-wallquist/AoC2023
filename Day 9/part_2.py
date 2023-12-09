from collections import deque


def diff_sequence(line):
    diff = deque([])
    for i in range(1, len(line)):
        diff.append(line[i] - line[i - 1])
    return diff


def get_sequences(line):
    seq = [line]
    while len(set(seq[-1])) > 1:
        seq.append(diff_sequence(seq[-1]))
    seq.append(deque([0 for i in range(len(seq[-1]) - 1)]))
    return seq


def extrapolate(seq):
    for s in range(len(seq) - 1, -1, -1):
        if s == len(seq) - 1:
            seq[s].appendleft(0)
        else:
            diff = seq[s + 1][0]
            seq[s].appendleft(seq[s][0] - diff)
    return seq[0][0]


predicted = []
with open("input.txt") as file:
    for line in file:
        line = deque([int(x) for x in line.strip().split(" ")])
        sequences = get_sequences(line)
        predicted.append(extrapolate(sequences))

print(sum(predicted))
