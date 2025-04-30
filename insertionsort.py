import matplotlib.pyplot as plt
import numpy as np
import time

count = 0
starttime = time.time()

start = 2
end = 100
amount = 50

sort = np.random.randint(start, end, amount)
x = np.arange(0, amount, 1)

n = len(sort)
for i in range(n):
    plt.title(f"total iterations: {count}, elapsed time: {round(time.time() - starttime, 2)}")
    plt.bar(x, sort)
    plt.pause(0.01)
    plt.clf()
    lowestindex = i
    for j in range(i, n):
        count = count + 1
        if sort[lowestindex] > sort[j]:
            lowestindex = j
    sort[i], sort[lowestindex] = sort[lowestindex], sort[i]

plt.show(block=False)
plt.close()

totaltime = round(time.time() - starttime, 2)

plt.title(f"total iterations: {count}, total time: {totaltime} seconds")
plt.bar(x, sort)
plt.pause(5)
plt.show(block=False)
plt.close('all')