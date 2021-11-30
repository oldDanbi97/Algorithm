def solution(citations):
    citations.sort()
    h_num_standard = citations[-1]
    answer = 0
    idx = 1
    while answer < h_num_standard:
        answer = len([i for i in citations if h_num_standard <= i])
        if idx > len(citations)-1:
            answer = len([i for i in citations if h_num_standard <= i])
            break
        if answer < h_num_standard:
            idx += 1
            h_num_standard = citations[-idx]
    return answer

print(solution([3, 3, 3, 4]))
