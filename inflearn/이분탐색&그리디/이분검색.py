n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt, rt = 0, n-1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] > m:
        rt = mid - 1
    elif a[mid] < m:
        lt = mid + 1
    else:
        print(mid + 1)
        break