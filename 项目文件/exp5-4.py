
def validate_sudoku(board):
    #1~9 的集合
    num = set(range(1,10))
    for i in board:
        if set(i) != num:
            return False
    for i in zip(*board):
        if set(i) != num:
            return False
    # 储存每个3X3的矩阵 验证 9个数字集合是否跟num集合相等
    for i in range(3,10,3):
        for j in range(3,10,3):
            if num != { (board[q][w])  for w in range(j-3, j) for q in range(i-3, i)}:
                return False
    return True
    
        

