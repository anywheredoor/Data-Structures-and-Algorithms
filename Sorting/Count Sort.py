array = [9, 6, 6, 6, 1, 2, 3, 8, 4, 5, 7, 0, 7, 3, 3, 3]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=" ")
