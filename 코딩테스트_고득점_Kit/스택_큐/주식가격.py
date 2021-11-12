def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        if i != len(prices) -1:
            for j in range(i+1, len(prices)):
                count += 1
                if prices[i] > prices[j]:
                    break
        answer.append(count)
    return answer