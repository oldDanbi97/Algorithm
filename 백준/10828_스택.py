import sys

stack = []
read = sys.stdin.readline
line_num = int(read().strip())
for i in range(line_num):
    command = read().strip().split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if not stack else 0)
    elif command[0] == 'top':
        print(stack[-1] if stack else -1)