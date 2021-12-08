def solution(name):
    answer = 0
    alpha_dict = {}
    for i in range(65, 91):
        alpha_dict[chr(i)] = i - 65
    i = 0
    name = list(name)
    while True:
        answer += min(alpha_dict[name[i]], alpha_dict['Z'] - alpha_dict[name[i]] + 1)
        name[i] = 'A'
        if name.count('A') == len(name) : return answer
        left, right = 1, 1
        for j in range(1, len(name)):
            if name[i-j] == 'A':
                left += 1
            else:
                break
        for j in range(1, len(name)):
            if name[i+j] == 'A':
                right += 1
            else:
                break
        if left < right:
            answer += left
            i -= left
        else:
            answer += right
            i += right
    return answer

print(solution("JAN"))