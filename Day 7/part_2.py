import re

card_map = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2,
}
hands = []
with open("input.txt") as input:
    for line in input:
        print(line.strip())
        hands.append((line.strip().split(" ")[0], int(line.strip().split(" ")[1])))


def hand_type(hand):
    if len(set(hand)) == 1:
        # Five-of-a-kind
        return 6

    if len(set(hand)) == 2:
        if 'J' in set(hand):
            # Five-of-a-kind
            return 6
        if (len(re.findall(r'' + list(set(hand))[0] + '', hand)) == 4 or
                len(re.findall(r'' + list(set(hand))[0] + '', hand)) == 1):
            # Four-of-a-kind
            return 5
        # Full house
        return 4

    if len(set(hand)) == 3:
        if (len(re.findall(r'' + list(set(hand))[0] + '', hand)) == 3 or
                len(re.findall(r'' + list(set(hand))[1] + '', hand)) == 3 or
                len(re.findall(r'' + list(set(hand))[2] + '', hand)) == 3):
            if 'J' in set(hand):
                # Four-of-a-kind
                return 5
            # Three-of-a-kind
            return 3
        if 'J' in set(hand):
            if hand.count('J') == 2:
                # Four-of-a-kind
                return 5
            # Full house
            return 4
        # Two pair
        return 2

    if len(set(hand)) == 4:
        if 'J' in set(hand):
            # Three-of-a-kind
            return 3
        # One pair
        return 1

    if len(set(hand)) == 5:
        if 'J' in hand:
            # One pair
            return 1
        # High card
        return 0


def swap(hand_list, index):
    current = hand_list[index]
    next = hand_list[index + 1]
    curr_type = hand_type(current[0])
    next_type = hand_type(next[0])

    if curr_type > next_type:
        hand_list[index + 1] = current
        hand_list[index] = next
        return True

    if curr_type == next_type:
        for i in range(len(current[0])):
            if card_map[current[0][i]] > card_map[next[0][i]]:
                hand_list[index + 1] = current
                hand_list[index] = next
                return True
            elif card_map[current[0][i]] < card_map[next[0][i]]:
                return False

    return False


def bubble_sort(hand_list):  #         >:)
    for i in range(len(hand_list)):
        swapped = False
        for j in range(0, len(hand_list) - i - 1):
            if swap(hand_list, j):
                swapped = True
        if not swapped:
            break


bubble_sort(hands)
s = 0
for ind in range(len(hands)):
    s += hands[ind][1] * (ind + 1)
print(s)
