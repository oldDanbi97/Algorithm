def solution(answers):
    math_give_up = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_num = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(len(math_give_up)):
            math_give_up_len = len(math_give_up[j])
            if answers[i] == math_give_up[j][i%math_give_up_len]:
                answer_num[j] += 1
    max_num = max(answer_num)
    answer = sorted([(i+1) for i in range(3) if answer_num[i] == max_num])
    return answer