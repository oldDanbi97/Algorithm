def solution(participant, completion):
    count = {}
    total = participant + completion
    for name in total:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1
    count = dict(filter(lambda x: x[1]%2 == 1, count.items()))
    return list(count.keys())[0]