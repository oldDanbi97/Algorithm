def solution(n, lost, reserve):
    for i in lost[:]:
        for j in reserve[:]:
            if i == j:
                lost.remove(i)
                reserve.remove(j)
    answer = n - len(lost)
    for i in range(n):
        if i in lost:
            if i-1 in reserve:
                answer += 1
                lost.remove(i)
                reserve.remove(i-1)
            elif i+1 in reserve:
                answer += 1
                lost.remove(i)
                reserve.remove(i+1)
    return answer

print(solution(9, [5,6,8,1,2], [2,3,1,4,8,9]))