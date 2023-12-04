import re

sum = 0
cards = []
with open("input.txt") as input:
    for line in input:
        num_matches = 0
        card_num = re.sub(' +', ' ', line.split(":")[0]).strip().split(" ")[1]
        win_nums = re.sub(' +', ' ', line.split(":")[1].split("|")[0]).strip().split(" ")
        my_nums = re.sub(' +', ' ', line.split(":")[1].split("|")[1]).strip().split(" ")

        for num in my_nums:
            if num in win_nums:
                num_matches += 1
        cards.append(list((int(card_num), num_matches, 1)))

for i, card in enumerate(cards):
    matches = card[1]
    number = card[2]
    for c in cards[i+1:]:
        if matches > 0:
            c[2] += number
            matches -= 1

for card in cards:
    sum += card[2]

print(sum)
