s = input()
stack = []
for i in s:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b/a)
print(stack.pop())