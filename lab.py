import matplotlib.pyplot as plt
import numpy as np
import random

N = 15
M = 10000

callProb = np.arange(0, 1, 0.005)

def averageTime(callProb):
    times = []
    for p in callProb:
        queue = [0]
        for j in range(1, M):
            slots = []
            for k in range(N):
                slots.append(random.choices([1, 0], weights = [p, 1 - p])[0])
            totalSlots = sum(slots)
            if queue[j - 1] <= 0 :
                queue.append(totalSlots)
            else:
                queue.append(queue[j - 1] - 1 + totalSlots)

        if p == 0:
            times.append(0)
        else:
            times.append(sum(queue) / p)
            
    return times

def collisionProbability(callProb):
    collisionProb = []
    for p in callProb:
        collisions = 0
        allCalls = 0
        for j in range(M):
            slots = []
            for k in range(N):
                slots.append(random.choices([1, 0], weights = [p, 1 - p])[0])
            if sum(slots) > 1:
                collisions += sum(slots)
            allCalls += sum(slots)
        if allCalls == 0:
            collisionProb.append(0);
        else:
            collisionProb.append(collisions/allCalls)
            
    return collisionProb

avgTime = averageTime(callProb)
collisionProb = collisionProbability(callProb)

plt.subplot(2,1,1)
plt.title('Зависимость среднего времени ожидания от вероятности звонка')
plt.ylabel('Среднее время ожидания')
plt.plot(callProb, avgTime)

plt.subplot(2,1,2)
plt.title('Зависимость вероятности коллизии от вероятности звонка')
plt.xlabel('Вероятность звонка')
plt.ylabel('Вероятность коллизии')
plt.plot(callProb, collisionProb)

plt.show()
