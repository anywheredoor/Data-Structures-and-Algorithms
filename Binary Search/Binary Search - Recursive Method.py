import sys

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("Not Found")
else:
    print(result + 1)

"""
10 7
1 3 5 7 9 11 13 15 17 19
Output: 4

10 7
1 3 5 6 9 11 13 15 17 19
Output: Not Found
"""
