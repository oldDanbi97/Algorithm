answer = 0
arr_len = 0
def dfs(numbers, target, idx, result):
    global answer
    if idx == arr_len:
        if target == result:
            answer += 1
        return
    else:
        dfs(numbers, target, idx+1, result + numbers[idx])
        dfs(numbers, target, idx+1, result - numbers[idx])

def solution(numbers, target):
    global answer
    global arr_len
    arr_len = len(numbers)
    dfs(numbers, target, 0, 0)
    return answer
