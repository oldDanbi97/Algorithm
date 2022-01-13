n, m = map(int, input().split())
people= list(map(int, input().split()))
people.sort()
cnt = 0
while people:
    p = people.pop()
    if people and p + people[0] <= m:
        people.pop(0)
    cnt += 1
print(cnt)