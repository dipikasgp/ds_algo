from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n-1, 0, -1):
        didSwap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = True
        if not didSwap:
            break