def solution(s):
    tuple_list = [i.split(',') for i in s[1:-2].replace('{','').split('},')]
    tuple_list = sorted(tuple_list, key= len)
    tmp_tupe = tuple_list[0]
    for i in tuple_list[1:]:
        if set(tmp_tupe) != set(i):
            for j in [k for k in i if k not in tmp_tupe]:
                tmp_tupe.append(j)
    return list(map(int, tmp_tupe))