def solution(board, moves):
    moves = [i-1 for i in moves]
    board_sort = []
    for i in range(len(board)):
        tmp_list = []
        for j in range(len(board)):
            if board[j][i] != 0:
                tmp_list.append(board[j][i])
        board_sort.append(tmp_list)
    answer = 0
    basket = []
    for i in moves:
        if len(board_sort[i]) > 0:
            tmp = board_sort[i].pop(0)
            basket.append(tmp)
            num = len(basket)
            if num > 1 and basket[num-1] == basket[num-2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer