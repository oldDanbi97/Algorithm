n = int(input())
sch = [list(map(int, input().split())) for _ in range(n)]
sch.sort(key= lambda x: (x[1], x[0]))
cur_meeting = sch[0]
cnt = 1
for i in range(1, n):
    if sch[i][0] >= cur_meeting[1]:
        cnt += 1
        cur_meeting = sch[i]
print(cnt)