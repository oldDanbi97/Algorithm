import sys
read = sys.stdin.readline
N = int(read().strip())
arr = list(map(int, read().strip().split()))
avg = int(sum(arr)/N + 0.5)
res = 1
min = 2147000000
for idx, x in enumerate(arr):
    tmp = abs(x-avg)
    if min > tmp:
        min = tmp
        score = x
        res = idx +1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)