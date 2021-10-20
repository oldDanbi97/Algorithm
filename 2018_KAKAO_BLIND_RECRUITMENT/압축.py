def solution(msg):
    answer = []
    alpha_list = []
    for i in range(65, 91):
        alpha_list.append(chr(i))
    
    word = ''
    while msg != '':
        for i in range(1, len(msg) + 1):
            if msg[:i] in alpha_list:
                word = msg[:i]
        answer.append(alpha_list.index(word) + 1)
        msg = msg[len(word):]
        if len(msg) > 0  and word + msg[0] not in alpha_list:
            alpha_list.append(word + msg[0])
    return answer