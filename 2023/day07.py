"""
https://adventofcode.com/2023/day/7
"""
import numpy as np

def main():
    with open("inputs\day07.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    print(p1(lines))
    print(p2(lines))

def p1(lines):
    ranks = []
    bids = []
    for line in lines:
        hand, bid = line.split(" ")
        if len(ranks) == 0:
            ranks.append(hand)
            bids.append(int(bid))
            continue
        for i in range(len(ranks)):
            result = compare_hands1(hand, ranks[i])
            if result > 0:
                ranks.insert(i, hand)
                bids.insert(i, int(bid))
                break
            if i == len(ranks) - 1:
                ranks.append(hand)
                bids.append(int(bid))

    return sum(np.array(list(range(1,len(bids)+1))) * np.array(bids))

def p2(lines):
    ranks = []
    bids = []
    for line in lines:
        hand, bid = line.split(" ")
        if len(ranks) == 0:
            ranks.append(hand)
            bids.append(int(bid))
            continue
        for i in range(len(ranks)):
            result = compare_hands2(hand, ranks[i])
            if result > 0:
                ranks.insert(i, hand)
                bids.insert(i, int(bid))
                break
            if i == len(ranks) - 1:
                ranks.append(hand)
                bids.append(int(bid))

    return sum(np.array(list(range(1,len(bids)+1))) * np.array(bids))

def compare_hands1(hand1, hand2):
    card_order = 'AKQJT98765432'

    hand_types = [1,2,3,4,5,6,7]

    def get_card_value(card):
        return card_order.index(card)

    type1, type2 = hand_types.index(get_hand_type1(hand1)), hand_types.index(get_hand_type1(hand2))
    if type1 != type2:
        return type1 - type2
    
    for card1, card2 in zip(hand1, hand2):
        value1, value2 = get_card_value(card1), get_card_value(card2)
        if value1 != value2:
            return value1 - value2

    return 0

def get_hand_type1(hand):
    if len(set(hand)) == 1:
        return 1
    elif len(set(hand)) == 2:
        counts = [hand.count(card) for card in set(hand)]
        if 4 in counts:
            return 2
        else:
            return 3
    elif len(set(hand)) == 3:
        counts = [hand.count(card) for card in set(hand)]
        if 3 in counts:
            return 4
        else:
            return 5
    elif len(set(hand)) == 4:
        return 6
    else:
        return 7

def compare_hands2(hand1, hand2):
    card_order = 'AKQT98765432'

    hand_types = [1,2,3,4,5,6,7]

    def get_card_value(card):
        return card_order.index(card)
    
    def replace_jokers(hand):
        if "J" in hand:
            hands = []
            for c in card_order:
                hands.append(hand.replace("J", c))

            results = []
            for hand in hands:
                results.append(get_hand_type1(hand))

            hand = hands[results.index(min(results))]
            return hand
        else:
            return hand

    def get_hand_type2(hand):
        hand = replace_jokers(hand)
        if len(set(hand)) == 1:
            return 1
        elif len(set(hand)) == 2:
            counts = [hand.count(card) for card in set(hand)]
            if 4 in counts:
                return 2
            else:
                return 3
        elif len(set(hand)) == 3:
            counts = [hand.count(card) for card in set(hand)]
            if 3 in counts:
                return 4
            else:
                return 5
        elif len(set(hand)) == 4:
            return 6
        else:
            return 7

    type1, type2 = hand_types.index(get_hand_type2(hand1)), hand_types.index(get_hand_type2(hand2))
    if type1 != type2:
        return type1 - type2

    for card1, card2 in zip(hand1, hand2):
        value1 = get_card_value(card1) if card1 != 'J' else get_card_value('2') + 1
        value2 = get_card_value(card2) if card2 != 'J' else get_card_value('2') + 1

        if value1 != value2:
            return value1 - value2

    return 0

main()