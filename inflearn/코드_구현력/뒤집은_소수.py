import sys
read = sys.stdin.readline
N = int(read().strip())
arr = list(map(int, read().strip().split()))
def reverse(x):
    res = 0
    while x > 0:
        t = x%10
        res = res*10 + t
        x //= 10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2):
        if x%i == 0:
            return False
    else:
        return True

for x in arr:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end= ' ')