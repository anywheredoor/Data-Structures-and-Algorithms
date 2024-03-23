import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value) # -value

    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) # -heapq.heappop(h)

    return result

result = heapsort([1, 9, 0, 2, 5, 3, 4, 7, 8, 6])

print(result)
