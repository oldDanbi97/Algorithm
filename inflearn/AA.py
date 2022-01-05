import sys
from collections import deque
sys.stdin=open(r"./inflearn/input.txt", "rt")
n = int(input())
a = [deque(map(int,input().split())) for _ in range(n)]
m = int(input())
b = [list(map(int,input().split())) for _ in range(m)]
for i in b:
    l, d, nn = i
    if d == 0:
        for _ in range(nn):
            a[l-1].append(a[l-1].popleft())
    else:
        for _ in range(nn):
            a[l-1].appendleft(a[l-1].pop())
res = 0
s, e = 0, n-1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)