import heapq

def solution(operations):
    answer = [0, 0]
    min_heap = []
    max_heap = []
    for i in operations:
        a, b = i.split(' ')
        if a == 'I':
            heapq.heappush(min_heap, int(b))
            heapq.heappush(max_heap, -int(b))
        elif a == 'D' and b == '1' and min_heap:
            num = -heapq.heappop(max_heap)
            min_heap.remove(num)
        elif a == 'D' and b == '-1' and max_heap:
            num = -heapq.heappop(min_heap)
            max_heap.remove(num )
    if len(min_heap) > 1 and len(max_heap) > 1:
        answer = [-int(heapq.heappop(max_heap)), int(heapq.heappop(min_heap))]
    elif len(operations) == 1 and min_heap and max_heap:
        answer = [min_heap[0], min_heap[0]]
    return answer