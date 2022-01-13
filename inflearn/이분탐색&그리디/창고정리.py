l = int(input())
height = list(map(int, input().split()))
m = int(input())
height.sort()
for i in range(m):
    height[-1] -= 1
    height[0] += 1
    height.sort()

print(height[-1]-height[0])