s = input()
n = len(s)
stack = []
cnt = 0
for i in range(n):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)