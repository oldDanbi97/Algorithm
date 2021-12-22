from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        person = people.pop()
        if people and person + people[0] <= limit:
            people.popleft()
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))