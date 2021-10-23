import re
def solution(files):
    answer = []
    tuple_list = []
    for file in files:
        m = re.match('([a-zA-z \.-]+)([0-9]+)(.*)', file)
        tuple_list.append(m.groups())
    answer = sorted(files, key = lambda x: (tuple_list[files.index(x)][0].lower(), int(tuple_list[files.index(x)][1]), files.index(x)))
    return answer