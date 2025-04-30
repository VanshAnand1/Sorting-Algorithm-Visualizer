import matplotlib.pyplot as plt
import numpy as np
import random
import is_sorted
import time

amount = 5
start = 2
end = 100
count = 0
starttime = time.time()

sort = np.random.randint(start, end, amount)
x = np.arange(0, amount, 1)

while is_sorted.is_sorted(sort) == False:
    plt.title(f"iterations: {count}, elapsed runtime: {round(time.time() - starttime, 2)} seconds")
    plt.bar(x, sort)
    plt.pause(0.01)
    plt.clf()
    random.shuffle(sort)
    count = count + 1
plt.show(block=False)
plt.close()

totaltime = round(time.time() - starttime, 2)
plt.title(f"total iterations: {count}, total time: {totaltime} seconds")
plt.bar(x, sort)
plt.pause(5)
plt.show(block=False)
plt.close('all')