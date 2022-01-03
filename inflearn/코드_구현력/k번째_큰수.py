from os import truncate
import sys
read = sys.stdin.readline
N, K = map(int, read().strip().split())
num = sorted(map(int, read().strip().split()), reverse=True)
result = []
end = False
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = num[i] + num[j] + num[k]
            result.append(sum)
            if len(set(result)) == K:
                print(result[-1])
                end = True
                break
        if end:
            break
    if end:
        break