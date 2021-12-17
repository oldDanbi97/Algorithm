import sys
from collections import deque
read = sys.stdin.readline
lstack, rstack = deque(read().strip()), deque()
line_num = int(read().strip())
for _ in range(line_num):
    cmd = read().strip().split()
    if cmd[0] == 'L' and lstack:
        rstack.appendleft(lstack.pop())
    elif cmd[0] == 'D' and rstack:
        lstack.append(rstack.popleft())
    elif cmd[0] == 'B' and lstack:
        lstack.pop()
    elif cmd[0] == 'P':
        lstack.append(cmd[1])
print(''.join(lstack + rstack))