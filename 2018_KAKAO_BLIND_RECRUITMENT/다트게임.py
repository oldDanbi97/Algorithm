def solution(str):
    num = []
    str = str.replace("10", "$")
    for index, s in enumerate(str):
        if s.isdecimal():
            num.append(int(s))
        elif s == "$":
            num.append(10)
        elif s == "*":
            if len(num) == 1:
                num[0] = num[0]*2
            else:
                num[len(num)-2] = num[len(num)-2]*2
                num[len(num)-1] = num[len(num)-1]*2
        elif s == "#":
            num[len(num)-1] = num[len(num)-1]*(-1)
        else:
            if s == "S":
                continue
            elif s == "D":
                num[len(num)-1] = num[len(num)-1]**2
            elif s == "T":
                num[len(num)-1] = num[len(num)-1]**3
    return sum(num)