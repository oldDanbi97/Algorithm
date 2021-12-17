import sys
time = list(map(int, sys.stdin.readline().strip().split()))
minute = (time[0] * 60  if time[0] != 0 else 24 * 60) + time[1] - 45
print(minute//60 if minute//60 != 24 else 0, minute%60)