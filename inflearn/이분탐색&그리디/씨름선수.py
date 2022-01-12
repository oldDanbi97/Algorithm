n = int(input())
player = [list(map(int, input().split())) for _ in range(n)]
player.sort(key=lambda x: -x[0])
cnt = 0
largest = 0
for i in range(n):
    if largest < player[i][1]:
        largest = player[i][1]
        cnt += 1
print(cnt)