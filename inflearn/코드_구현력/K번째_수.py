import sys
read = sys.stdin.readline
N, K = map(int, read().strip().split())
num = list(map(int, read().strip().split()))
res = set()
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            res.add(num[i] + num[j] + num[k])
res = sorted(list(res),reverse=True)
print(res[K-1])