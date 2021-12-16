import sys

read = sys.stdin.readline
line_num = int(read().strip())
for _ in range(line_num):
    print(' '.join([''.join(list(reversed(i))) for i in read().strip().split()]))