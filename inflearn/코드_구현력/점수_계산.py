import sys
N = int(input())
answer = list(map(int, input().split()))
res = 0
plus = 1
for i in answer:
    if i == 1:
        res += plus
        plus += 1
    elif i == 0:
        plus = 1
print(res)