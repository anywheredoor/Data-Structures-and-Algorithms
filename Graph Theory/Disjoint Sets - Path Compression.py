def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

for i in range(1, v + 1):
    print(parent[i], end=" ")

"""
-INPUT-
6 4
1 4
2 3
2 4
5 6

-OUTPUT-
1 1 1 1 5 5 
1 1 1 1 5 5
"""
