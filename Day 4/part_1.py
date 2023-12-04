import re

sum = 0
with open("input.txt") as input:
    for line in input:
        card_sum = 0
        num_matches = 0
        win_nums = re.sub(' +', ' ', line.split(":")[1].split("|")[0]).strip().split(" ")
        my_nums = re.sub(' +', ' ', line.split(":")[1].split("|")[1]).strip().split(" ")

        for num in my_nums:
            if num in win_nums:
                num_matches += 1
                if num_matches == 1:
                    card_sum += 1
                else:
                    card_sum *= 2
        sum += card_sum

print(sum)
