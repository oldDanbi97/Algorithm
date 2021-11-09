def solution(genres, plays):
    answer = []
    music = {}
    for index, genre, play in zip(range(len(genres)), genres, plays):
        if genre not in music:
            music[genre] = []
        music[genre].append((index, play))

    sum_arr = {}
    for genre, list in music.items():
        sum = 0
        for pair in list:
            sum +=pair[1]
        sum_arr[genre] = sum

    music = sorted(music.items(), key = lambda x: sum_arr[x[0]], reverse=True)
    sort_music = []
    for pair in music:
        sort_music.append(sorted(pair[1], key= lambda x: x[1], reverse=True))
    
    answer = sort_list(sort_music)
    return answer

def sort_list(answer):
    tmp_arr = []
    for song_list in answer:
        if len(song_list) < 2:
            tmp_arr.append(song_list[0][0])
        else:
            if song_list[0][1] == song_list[1][1]:
                if song_list[0][0] < song_list[1][0]:
                    tmp_arr.append(song_list[0][0])
                    tmp_arr.append(song_list[1][0])
                else:
                    tmp_arr.append(song_list[1][0])
                    tmp_arr.append(song_list[0][0])
            else:
                tmp_arr.append(song_list[0][0])
                tmp_arr.append(song_list[1][0])
    return tmp_arr