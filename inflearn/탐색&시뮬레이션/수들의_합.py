n, m = map(int, input().split())
a = list(map(int, input().split()))
tot = a[0]
lt, rt = 0, 1
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    elif tot > m:
        tot -= a[lt]
        lt += 1
print(cnt)