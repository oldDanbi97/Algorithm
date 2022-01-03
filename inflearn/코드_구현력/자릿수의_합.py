import sys
def digit_sum(x):
    result = 0
    while x > 0:
        result += x%10
        x //= 10
    return result

read = sys.stdin.readline
N = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))
max = -2147000000
res = 0
for i in arr:
    tmp = digit_sum(i)
    if max < tmp:
        max = tmp
        res = i
print(res)