def solution(str1, str2):
    list = []
    inter_set = set()
    union_set = set()
    inter = 0
    union = 0
    for i in [str1.lower(), str2.lower()]:
        arr = []
        for j in range(len(i)-1):
            if i[j].isalpha() and i[j+1].isalpha():
                arr.append(i[j]+i[j+1])
        list.append(arr)
    inter_set = set(list[0]) & set(list[1])
    union_set = set(list[0]) | set(list[1])
    for i in inter_set:
        inter += min(list[0].count(i), list[1].count(i))
    for i in union_set:
        union += max(list[0].count(i), list[1].count(i))
    if union == 0:
        return 65536
    else:
        return int(inter/union * 65536)