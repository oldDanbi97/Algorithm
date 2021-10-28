def solution(n, arr1, arr2):
    list1 = [format(i, 'b').zfill(n) for i in arr1]
    list2 = [format(i, 'b').zfill(n) for i in arr2]
    answer = []
    for i in range(n):
        str = []
        for j in range(n):
            if list1[i][j] == '1' or list2[i][j] == '1':
                str.append('#')
            else:
                str.append(' ')
        answer.append(''.join(str))
    return answer
