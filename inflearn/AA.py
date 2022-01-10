import sys
sys.stdin=open(r"./inflearn/input.txt", "r")
n, m = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
print(h)
