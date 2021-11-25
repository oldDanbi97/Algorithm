from itertools import permutations

def solution(numbers):
    per_result = []
    for i in range(1, len(numbers)+1):
        per_result.extend(list(permutations(numbers, i)))
    per_result = list(filter(lambda x: x >1, set([int(''.join(i)) for i in set(per_result)])))
    answer = len([i for i in per_result if is_prime_num(i)])
    return answer

def is_prime_num(num):
    result = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result

print(solution("17"))