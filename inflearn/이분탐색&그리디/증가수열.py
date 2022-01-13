from collections import deque
n = int(input())
arr = deque(map(int, input().split()))
ep = 0
res = []
while arr and (ep < arr[0] or ep < arr[-1]):
    if len(arr) == 1:
        if ep < arr[0]:
            res.append('L')
        break
    elif ep < arr[0] < arr[-1] or arr[0] > ep > arr[-1]:
        ep = arr.popleft()
        res.append('L')
    elif ep < arr[-1] < arr[0] or arr[-1] > ep > arr[0]:
        ep = arr.pop()
        res.append('R')
print(len(res))
print(''.join(res))