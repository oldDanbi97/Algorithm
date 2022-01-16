n, m = map(int, input().split())
n = list(map(int, str(n)))
stack = []
for i in n:
    while stack and m > 0 and stack[-1] < i:
        stack.pop()
        m -= 1
    stack.append(i)
if m != 0:
    stack = stack[:-m]
print(''.join(map(str, stack)))