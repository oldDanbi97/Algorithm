N = int(input())
for i in range(N):
    word = input().lower()
    tmp = []
    stack = list(word)
    result = 'NO'
    while stack:
        tmp.append(stack.pop())
    if ''.join(tmp) == word:
        result = 'YES'
    print('#%d %s'%(i+1, result))