def solution(N, stages):
    answer = []
    ratio = []
    for n in range(1, N+1):
        challenge_user = len([i for i in stages if i>=n])
        success_user = len([i for i in stages if i> n])
        tmp_ratio = 0
        if challenge_user == 0:
            tmp_ratio =0
        else:
            tmp_ratio = (challenge_user-success_user)/challenge_user
        ratio.append([n, tmp_ratio])
    ratio = sorted(ratio, key=lambda x: -x[1])
    answer = [i[0] for i in ratio]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))