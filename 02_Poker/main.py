import random
import time
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        diff = end_time - start_time
        print(f"Finished {func.__name__} in {diff:.8f} secs")
        return value

    return wrapper_timer

@timer
def royal_flush(list, statistics):
    royal_flush_values = [0, 9, 10, 11, 12]
    list.sort()

    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

        # check for royal flush values
        if list[i - 1] % 13 != royal_flush_values[i - 1]:
            return False

    statistics['royal_flush'] += 1
    return True

@timer
def straight(list, statistics):
    mods = []
    for i in range(0, 5):
        mods.append(list[i] % 13)
    mods.sort()

    for i in range(1, 5):
        if mods[i - 1] + 1 != mods[i]:
            return False
    statistics['straight'] += 1
    return True

@timer
def straight_flush(list, statistics):
    list.sort()
    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

        # check for ascending values
        if list[i - 1] + 1 != list[i]:
            return False

    statistics['straight_flush'] += 1
    return True

@timer
def flush(list, statistics):
    for i in range(1, 5):
        # check for same colors
        if list[i - 1] // 13 != list[i] // 13:
            return False

    statistics['flush'] += 1
    return True

@timer
def four_of_a_kind(list, statistics):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 4:
        statistics['four_of_a_kind'] += 1
        return True
    return False

@timer
def three_of_a_kind(list, statistics):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 3:
        statistics['three_of_a_kind'] += 1
        return True
    return False

@timer
def pair(list, statistics):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 2:
        statistics['pair'] += 1
        return True
    return False

@timer
def two_pair(list, statistics):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 2 and occ.most_common()[1][1] == 2:
        statistics['two_pair'] += 1
        return True
    return False

@timer
def full_house(list, statistics):
    mods = []
    for i in range(1, 6):
        mods.append(list[i - 1] % 13)
    mods.sort()
    occ = Counter(mods)

    if occ.most_common()[0][1] == 3 and occ.most_common()[1][1] == 2:
        statistics['full_house'] += 1
        return True
    return False

@timer
def high_card(statistics):
    statistics['high_card'] += 1
    return True

def main():
    statistics = {
        'royal_flush': 0,
        'straight_flush': 0,
        'four_of_a_kind': 0,
        'full_house': 0,
        'flush': 0,
        'straight': 0,
        'three_of_a_kind': 0,
        'two_pair': 0,
        'pair': 0,
        'high_card': 0,
    }

    cards_amount = 52

    pull_cards_amount = 5
    tries = 1_000

    print('BEGIN POKER \n')

    for i in range(tries):
        current_pair = random.sample(range(0, cards_amount), pull_cards_amount)

        if not royal_flush(current_pair, statistics):
            if not straight_flush(current_pair, statistics):
                if not four_of_a_kind(current_pair, statistics):
                    if not full_house(current_pair, statistics):
                        if not flush(current_pair, statistics):
                            if not straight(current_pair, statistics):
                                if not three_of_a_kind(current_pair, statistics):
                                    if not two_pair(current_pair, statistics):
                                        if not pair(current_pair, statistics):
                                            high_card(statistics)
        print('')
    print('END POKER\n')
    for i in statistics:
        statistics[i] = (statistics[i] / tries) * 100

    # https://en.wikipedia.org/wiki/Poker_probability#5-card_poker_hands
    wikipedia_x = [0.000154, 0.00139, 0.02401, 0.1441, 0.1965, 0.3925, 2.1128, 4.7539, 42.2569, 50.1177]

    print(f"Wikipedia %\t\t\t|\t\tEgger %\t\t|\t\tCard Hand")
    print(f"--------------------|-----------------------|-----------------------")

    j = 0
    for i in statistics:
        print(f"{wikipedia_x[j]:.6f}\t\t\t|\t\t{statistics[i]:.6f}\t\t|\t\t{i}")
        j += 1
    print(f"tries={tries}")

    """
    plt.bar(statistics.keys(), wikipedia_x, color="red")
    plt.xticks(rotation=45)
    plt.title("Wikipedia")
    plt.show()
    
    plt.bar(statistics.keys(), statistics.values())
    plt.xticks(rotation=45)
    plt.show()
    """


if __name__ == '__main__':
    main()
