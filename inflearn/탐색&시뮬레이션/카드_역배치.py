n = [(i+1) for i in range(20)]
for i in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        n[s+i-1], n[e-i-1] = n[e-i-1], n[s+i-1]
print(*n)