import sys
sys.stdin=open(r"./inflearn/input.txt", "r")
l = int(input())
height = list(map(int, input().split()))
m = int(input())
height.sort()
print(height)
i = 0
while m > 0:
    differ = height[-i-1] - height[i]
    m -= differ
    i += 1