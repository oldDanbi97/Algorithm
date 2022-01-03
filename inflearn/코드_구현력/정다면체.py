import sys
read = sys.stdin.readline
N, M = map(int, read().strip().split())
cnt = [0] * (N + M + 1)
for i in range(1, N+1):
    for j in range(1, M+1):
        cnt[i+j] += 1
max = -2147000000
for i in range(N + M + 1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(N + M + 1):
    if cnt[i] == max:
        print(i, end= ' ')