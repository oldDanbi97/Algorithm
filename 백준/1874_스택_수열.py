import sys
read = sys.stdin.readline
num_arr = [i + 1 for i in range(int(read().strip()))]
complete_num, stack, answer = [], [], []
for _ in range(len(num_arr)):
    complete_num.append(int(read().strip()))
for i in range(len(complete_num)):
    while not stack or (stack and stack[-1] != complete_num[i]):
        if not num_arr: break
        stack.append(num_arr.pop(0))
        answer.append('+')
    if complete_num and stack[-1] == complete_num[i]:
        stack.pop()
        answer.append('-')
if stack: answer = 'NO'
else: answer = '\n'.join(answer)
print(answer)