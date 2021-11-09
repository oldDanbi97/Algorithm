def solution(clothes):
    answer = 0
    dic = {}
    for pair in clothes:
        if pair[1] not in dic:
            dic[pair[1]] = 2
        else:
            dic[pair[1]] += 1
    add = 1
    for item in dic.values():
        add *= item
    answer += add
    return answer -1