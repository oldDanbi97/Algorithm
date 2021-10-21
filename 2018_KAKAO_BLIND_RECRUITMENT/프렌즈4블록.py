def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    answer = 0
    while True:
        delete_set = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] and board[i][j+1] == board[i+1][j+1] and board[i+1][j] == board[i+1][j+1] and board[i+1][j+1] != 'x':
                    delete_set.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
        for idx in delete_set:
            board[idx[0]][idx[1]] = 'x'
        board = down(m, n, board)
        answer += len(delete_set)
        if len(delete_set) == 0:
            break
    return answer
def down(m, n, board):
    chk = False
    for i in range(m-1):
        for j in range(n):
            if board[i][j] != 'x' and board[i + 1][j] == 'x':
                board[i + 1][j] = board[i][j]
                board[i][j] = 'x'
                chk = True
    if chk:
        down(m, n, board)
    return board
