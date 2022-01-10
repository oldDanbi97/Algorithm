n, m = map(int, input().split())
a = list(map(int, input().split()))
def mcount(size):
    tmpM = m
    cnt = 0
    i = 0
    while tmpM > 0:
        tmpSize = size
        while i < n:
            if tmpSize < a[i]:
                break
            else:
                tmpSize -= a[i]
                i += 1
                cnt += 1
        tmpM -= 1
    return cnt
lt, rt = 0, max(a) * n
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mcount(mid) < n:
        lt = mid + 1
    else:
        res = mid
        rt = mid - 1
print(res)