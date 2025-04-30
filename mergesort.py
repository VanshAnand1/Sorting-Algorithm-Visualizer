import matplotlib.pyplot as plt
import numpy as np
import time

# implement mergesort
def merge(left, right):
    sorted = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i = i + 1
        else:
            sorted.append(right[j])
            j = j + 1
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    plt.title(f"elapsed runtime: {round(time.time() - starttime, 2)} seconds")
    plt.bar(x, sort)
    plt.pause(0.01)
    plt.clf()
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    return merge(left, right)

amount = 100
start = 2
end = 100
starttime = time.time()

sort = np.random.randint(start, end, amount)
x = np.arange(0, amount, 1)

n = len(sort)
sort = mergesort(sort)
sort = [int(x) for x in sort]

totaltime = round(time.time() - starttime, 2)
plt.title(f"total time: {totaltime} seconds")
plt.bar(x, sort)
plt.pause(5)
plt.show(block=False)
plt.close('all')