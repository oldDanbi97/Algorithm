import sys

read = sys.stdin.readline
line_num = int(read().strip())
for _ in range(line_num):
    i = read().strip()
    stack = []
    for j in i:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
                break
    print('NO' if stack else 'YES')