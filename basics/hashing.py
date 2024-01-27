from typing import List


def getFrequencies(v):
    d = dict()
    for ele in v:
        if ele in d.keys():
            d[ele] += 1
        else:
            d[ele] = 1

    max = 0
    min = 9999
    max_k = 0
    min_k = 0
    for key, val in d.items():
        # print(key, val)
        if val > max:
            max = val
            max_k = key
        if val < min:
            min = val
            min_k = key
    return ([max_k, min_k])