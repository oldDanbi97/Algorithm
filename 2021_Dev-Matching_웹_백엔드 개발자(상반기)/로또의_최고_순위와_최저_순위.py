def solution(lottos, win_nums):
    zero_num = lottos.count(0)
    _lottos = [i for i in lottos if i != 0]
    _win_nums = [i for i in win_nums if i in _lottos]
    min_num = len(_win_nums)
    answer = [min_num + zero_num, min_num]
    return list(map(getGrade, answer))

def getGrade(num):
    grade = 6
    if num == 6: grade = 1
    elif num == 5: grade =2
    elif num == 4: grade = 3
    elif num == 3: grade = 4
    elif num == 2: grade = 5
    return grade

print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))