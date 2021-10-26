import re
def solution(new_id):
    answer = ''.join([i for i in new_id.lower() if i.isalpha() or i.isdecimal() or i in ['-','_','.']])
    answer = re.sub('\.{2,}', '.',answer)
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[len(answer)-1] == '.': answer = answer[:len(answer)-1]
    if answer == '': answer = 'a'
    elif len(answer) >= 16:
        answer = answer[:15]
        if answer[len(answer)-1] == '.': answer = answer[:len(answer)-1]
    if len(answer) <= 2:
       answer += answer[len(answer)-1]*(3-len(answer))
    return answer
