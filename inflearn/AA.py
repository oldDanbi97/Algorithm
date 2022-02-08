import sys
from collections import deque
sys.stdin=open(r"./inflearn/input.txt", "r")
n, m = map(int, input().split())
p = list(map(int, input().split()))
queue = deque([(i, p[i]) for i in range(n)])
cnt = 0
while True:
    cur = queue.popleft()
    if any(cur[1] < x[1] for x in queue):
        queue.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)