import sys
sys.stdin=open(r"./inflearn/input.txt", "rt")
read = sys.stdin.readline
n, k = map(int, read().strip().split())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)