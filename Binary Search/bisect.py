from bisect import bisect_left, bisect_right

array = [1, 2, 4, 4, 8]
target = 4

print(bisect_left(array, target)) # 2
print(bisect_right(array, target)) # 4
