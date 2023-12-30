def get_diag_1(i, j):
    return i + j

def get_diag_2(i, j):
    return i - j

def can_disable_position(i: int, j: int, available_rows: set, available_cols: set, available_diag1: set, available_diag2: set):
    if i not in available_rows:
        return False
    if j not in available_cols:
        return False
    if get_diag_1(i, j) not in available_diag1:
        return False
    if get_diag_2(i, j) not in available_diag2:
        return False
    
    return True
    
def disable_position(i: int, j: int, available_rows: set, available_cols: set, available_diag1: set, available_diag2: set):
    available_rows.remove(i)
    available_cols.remove(j)
    available_diag1.remove(get_diag_1(i, j))
    available_diag2.remove(get_diag_2(i, j))

def enable_position(i: int, j: int, available_rows: set, available_cols: set, available_diag1: set, available_diag2: set):
    available_rows.add(i)
    available_cols.add(j)
    available_diag1.add(get_diag_1(i, j))
    available_diag2.add(get_diag_2(i, j))

def find_ways_rec(positions: list, current_row: int, available_rows: set, available_cols: set, available_diag1: set, available_diag2: set, result: list):
    if len(positions) == 8:
        result.append(positions.copy())
        
    for current_col in available_cols.copy():
        queen = (current_row, current_col)
        if not can_disable_position(current_row, current_col, available_rows, available_cols, available_diag1, available_diag2):
            continue
        
        positions.append(queen)
        
        disable_position(current_row, current_col, available_rows, available_cols, available_diag1, available_diag2)
        find_ways_rec(positions, current_row + 1, available_rows, available_cols, available_diag1, available_diag2, result)

        enable_position(current_row, current_col, available_rows, available_cols, available_diag1, available_diag2)
        positions.pop()
        
def print_result(positions: list):
    board = [['o' for j in range(8)] for i in range(8)]   
    
    for i,j in positions:
        board[i][j] = 'x'
        
    for r in board:
        print(''.join(r))
    print()

def find_ways():
    available_cols = set([i for i in range(8)])
    available_rows = set([i for i in range(8)])
    available_diag1 = set([i for i in range(15)])
    available_diag2 = set([i for i in range(-7,8)])
    result = []
    find_ways_rec([], 0, available_rows, available_cols, available_diag1, available_diag2, result)
    
    for r in result[:10]:
        print_result(r)
        
    print(len(result))
    
find_ways()