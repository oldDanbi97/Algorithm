def solution(m, musicinfos):
    answer = ''
    m = m.replace('C#','$').replace('D#','%').replace('F#','^').replace('G#','&').replace('A#','(')
    title_list = []
    m_list = [i.split(',') for i in musicinfos]
    for i in m_list:
        i[3] = i[3].replace('C#','$').replace('D#','%').replace('F#','^').replace('G#','&').replace('A#','(')
        start_time = [int(t) for t in i[0].split(':')]
        end_time = [int(t) for t in i[1].split(':')]
        time = -start_time[0]*60 - start_time[1] + end_time[0]*60 + end_time[1]
        if len(i[3]) < time:
            melody = list(i[3])
            idx = 0
            while len(melody) != time:
                melody.append(i[3][idx])
                idx += 1
                if idx > len(i[3])-1: idx = 0
            if m in ''.join(melody):
                title_list.append([i[2], time])
        elif len(i[3]) > time:
            if m in i[3][:time]:
                title_list.append([i[2], time])
        else:
            if m in i[3]:
                title_list.append([i[2], time])
        if len(title_list) == 0: answer = '(None)'
        else: answer = sorted(title_list, key= lambda x: -x[1])[0][0]
    return answer
print(solution(	"A#", ["13:00,13:02,HAPPY,B#A#"]))