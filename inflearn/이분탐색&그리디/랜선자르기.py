n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
lt, rt = 1, max(a)
res = 0
def lcount(cm):
    cnt = 0
    for i in a:
        cnt += i//cm
    return cnt
while lt <= rt:
    mid = (lt + rt) // 2
    if lcount(mid) >= m:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)