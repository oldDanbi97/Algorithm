import math
def solution(progresses, speeds):
    completion_period = [[idx, math.ceil((100-progress)/speed)] for idx, (progress, speed) in enumerate(zip(progresses, speeds))]
    cnt = 0
    answer = []
    max_day = 0
    for id, day in completion_period:
        if cnt == 0:
            cnt += 1
            max_day = day
        else:
            if max_day >= day:
                cnt += 1
            elif max_day < day:
                answer.append(cnt)
                cnt = 1
                max_day = day
        if id == len(completion_period) - 1:
            answer.append(cnt)
    return answer
