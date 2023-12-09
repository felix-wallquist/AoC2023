def diff_sequence(line):
    diff = []
    for i in range(1, len(line)):
        diff.append(line[i] - line[i - 1])
    return diff


def get_sequences(line):
    seq = [line]
    while len(set(seq[-1])) > 1:
        seq.append(diff_sequence(seq[-1]))
    seq.append([0 for i in range(len(seq[-1]) - 1)])
    return seq


def extrapolate(seq):
    for s in range(len(seq) - 1, -1, -1):
        if s == len(seq) - 1:
            seq[s].append(0)
        else:
            diff = seq[s + 1][-1]
            seq[s].append(seq[s][-1] + diff)
    return seq[0][-1]


predicted = []
with open("input.txt") as file:
    for line in file:
        line = [int(x) for x in line.strip().split(" ")]
        sequences = get_sequences(line)
        predicted.append(extrapolate(sequences))

print(sum(predicted))
