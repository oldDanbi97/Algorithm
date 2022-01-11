n, m = map(int, input().split())
h = [int(input()) for _ in range(n)]

def horse_count(l):
    cnt = 1
    ep = h[0]
    for i in range(1, n):
        if h[i]-ep >= l:
            cnt += 1
            ep = h[i]
    return cnt

h.sort()
lt = 1
rt = h[-1]
while lt <= rt:
    mid = (lt+rt)//2
    if horse_count(mid) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
