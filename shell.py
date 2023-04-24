import random

while True:
    a = int(input())
    if a == 0:
        data = random.sample(range(100), 20)
        last_index = len(data)
        step = len(data)//2
        while step > 0:
            for i in range(step, last_index, 1):
                delta = i - step
                while delta >= 0 and data[delta] > data[i]:
                    data[delta], data[i] = data[i], data[delta]
                    delta = delta - step
            step //= 2
        print(data)
    if a == 1:
        break
