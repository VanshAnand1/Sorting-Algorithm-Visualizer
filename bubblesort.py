import matplotlib.pyplot as plt
import numpy as np
import time

amount = 100
start = 2
end = 100
count = 0
starttime = time.time()

sort = np.random.randint(start, end, amount)
x = np.arange(0, amount, 1)

n = len(sort)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        count = count + 1
        plt.title(f"iterations: {count}, elapsed runtime: {round(time.time() - starttime, 2)} seconds")
        plt.bar(x, sort)
        plt.pause(0.01)
        plt.clf()
        if sort[j] > sort[j + 1]:
            sort[j], sort[j + 1] = sort[j + 1], sort[j]
            swapped = True
    if swapped == False:
        break

plt.show(block=False)
plt.close()

totaltime = round(time.time() - starttime, 2)
plt.title(f"total iterations: {count}, total time: {totaltime} seconds")
plt.bar(x, sort)
plt.pause(5)
plt.show(block=False)
plt.close('all')