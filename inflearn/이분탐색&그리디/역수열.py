n = int(input())
a = list(map(int, input().split()))
seq = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1
print(*seq)