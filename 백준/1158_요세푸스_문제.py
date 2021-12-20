import sys
from collections import deque
read= sys.stdin.readline
N, K = map(int, read().strip().split())
queue = deque([i+1 for i in range(N)])
answer = []
while queue:
    queue.rotate(-K+1)
    answer.append(str(queue.popleft()))
print('<'+', '.join(answer) + '>')