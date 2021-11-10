def solution(array, commands):
    answer = []
    for arr in commands:
       answer.append(sorted(array[arr[0]-1:arr[1]], key=lambda x: x)[arr[2]-1])
    return answer