import sys
sys.stdin=open(r"./inflearn/input.txt", "rt")
read = sys.stdin.readline
N = int(read().strip())
ch = [0] * (N + 1)
cnt = 0
for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, N+1, i):
            ch[j] = 1
print(cnt)