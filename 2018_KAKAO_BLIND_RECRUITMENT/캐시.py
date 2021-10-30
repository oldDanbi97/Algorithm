from collections import deque
def solution(cacheSize, cities):
    answer = 0
    deq = deque([], maxlen=cacheSize)
    cities = [i.lower() for i in cities]
    while len(cities) > 0:
        city = cities.pop(0)
        if city not in deq:
            answer += 5
        elif deq[0] == city:
            answer += 1
        else:
            answer += 1
            deq.remove(city)
        deq.append(city)
    return answer