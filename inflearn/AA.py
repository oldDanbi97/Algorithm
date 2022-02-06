import sys
from collections import deque
sys.stdin=open(r"./inflearn/input.txt", "r")
n, k = map(int, input().split())
queue = deque(list(range(1, n+1)))
while queue:
    for _ in range(k-1):
        cur = queue.popleft()
        queue.append(cur)
    queue.popleft()
    if len(queue) == 1:
        print(queue.pop())
