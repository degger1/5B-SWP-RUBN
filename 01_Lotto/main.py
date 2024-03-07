import random
import matplotlib.pyplot as plt
import numpy as np


def gamble(n, res):
    if n <= 0:
        print("number must be positive")
        return

    max = 45
    num = []

    for i in range(max):
        num.append(i)

    for i in range(n):
        index = random.randint(0, max - 1 - i)

        old = num[index]
        new = num[max - 1 - i]
        num[index], num[max - 1 - i] = new, old
        res.append(old)

    return res


def statistic(res, dic):
    for i in range(len(res)):
        dic[res[i]] = dic[res[i]] + 1


dic = {}
for x in range(45):
    dic[x] = 0

tries = 1000000
for n in range(tries):
    res = []
    gamble(6, res)
    statistic(res, dic)

plt.bar(dic.keys(), dic.values())
plt.title("lottery numbers, n=" + str(tries))
plt.xlabel("numbers")
plt.ylabel("occurrence")
plt.show()

# https://www.w3schools.com/python/matplotlib_bars.asp
