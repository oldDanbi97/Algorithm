def solution(brown, yellow):
    answer = []
    whole_block_num = brown + yellow
    for i in range(1, whole_block_num):
        if whole_block_num % i == 0:
            answer = sorted([whole_block_num // i, i],reverse=True)
            if (answer[0]-2)*2 + answer[1]*2 == brown and (answer[0]-2)*(answer[1]-2) == yellow:
                break
    return answer

print(solution(24, 24))