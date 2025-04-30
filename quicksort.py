import matplotlib.pyplot as plt
import numpy as np
import time

starttime = time.time()

def quicksort(arr, count=0):
    if len(arr) <= 1:
        return count
    count = quicksort(arr[1:], count)
    i = 0
    while i + 1 < len(arr):
        count = count + 1
        plt.title(f"total iterations: {count}, elapsed runtime: {round(time.time() - starttime, 2)} seconds")
        plt.bar(x, sort)
        plt.pause(0.01)
        plt.clf()
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i = i + 1 
    return count

amount = 50
start = 2
end = 100

sort = np.random.randint(start, end, amount)
x = np.arange(0, amount, 1)
count = quicksort(sort)

plt.title(f"total iterations: {count}, total runtime: {round(time.time() - starttime, 2)} seconds")
plt.bar(x, sort)
plt.pause(5)
plt.show(block=False)
plt.close('all')
