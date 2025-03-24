import heapq
list1 = [5, 4, 9, 1, 5, 100]
heapq.heapify(list1)
heapq.heappop(list1)
print(heapq.nlargest(1, list1))
print(list1)