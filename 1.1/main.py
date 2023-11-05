import sys
import random

N = int(sys.argv[1])

arr = []
for i in range(0, N):
    arr.append(random.random())

for i in range(0, N - 1):
    for j in range(0, N - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)