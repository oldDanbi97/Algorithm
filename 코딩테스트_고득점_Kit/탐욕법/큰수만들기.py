def solution(number, k):
    answer = []
    for i in number:
        print(answer, i)
        while answer and answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
        answer.append(i)
    return ''.join(answer[:len(number)-k])

print(solution("1231234", 3))