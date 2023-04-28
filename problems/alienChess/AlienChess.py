
def get_pawn_possible_moves(grid, row, col):
    moves = []
    if 0 < row < len(grid):
        if col > 0 and grid[row-1][col-1] != '-':
            moves.append((row-1, col-1))
        if col < 7 and grid[row-1][col+1] != '-':
            moves.append((row-1, col+1))
    return moves

def get_rook_possible_moves(grid, row, col):
    moves = []
    # check top
    for r in range(row-1, -1, -1):
        if grid[r][col] != '-':
            moves.append((r, col))
            break
    # check bottom
    for r in range(row+1, 8):
        if grid[r][col] != '-':
            moves.append((r, col))
            break
    # check left
    for c in range(col-1, -1, -1):
        if grid[row][c] != '-':
            moves.append((row, c))
            break
    # check right
    for c in range(col+1, 8):
        if grid[row][c] != '-':
            moves.append((row, c))
            break
    return moves

def get_bishop_possible_moves(grid, row, col):
    moves = []
    # check top left
    i = 1
    while row-i>=0 and col-i>=0:
        if grid[row-i][col-i] != '-':
            moves.append((row-i, col-i))
            break
        i += 1
    # check top right
    i = 1
    while row-i>=0 and col+i<8:
        if grid[row-i][col+i] != '-':
            moves.append((row-i, col+i))
            break
        i += 1
    # check bottom left
    i = 1
    while row+i<8 and col-i>=0:
        if grid[row+i][col-i] != '-':
            moves.append((row+i, col-i))
            break
        i += 1
    # check bottom right
    i = 1
    while row+i<8 and col+i<8:
        if grid[row+i][col+i] != '-':
            moves.append((row+i, col+i))
            break
        i += 1
    return moves

def get_knight_possible_moves(grid, row, col):
    moves = []
    if row + 2 < 8 and col + 1 < 8 and grid[row+2][col+1] != '-':
        moves.append((row+2, col+1))
    
    offsets = [
        (-1, -2),
        (1, -2),
        (-2, -1),
        (2, -1),
        (-2, 1),
        (2, 1),
        (-1, 2),
        (1, 2),  
    ]
    
    for offset in offsets:
        possibleMove = (offset[0] + row, offset[1] + col)
        # Check row bounds
        if possibleMove[0] < 0 or possibleMove[1] >= len(grid):
            continue
        
        # Check col bounds
        if possibleMove[1] < 0 or possibleMove[1] >= len(grid[possibleMove[0]]):
            continue
        
        # Check if space is empty:
        if grid[possibleMove[0]][possibleMove[1]] == '-':
            continue
        
        moves.append(possibleMove)
    
    return moves

possible_moves = {
    'P': get_pawn_possible_moves,
    'R': get_rook_possible_moves,
    'B': get_bishop_possible_moves,
    'K': get_knight_possible_moves
}

def find_in_grid(grid, val):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == val:
                return (row, col)

def can_win(grid, move_type = 'P'):
    super_location = find_in_grid(grid, 'S')
    moves = possible_moves[move_type](grid, super_location[0], super_location[1])
    grid[super_location[0]][super_location[1]] = '-'
    for move in moves:
        target_piece = grid[move[0]][move[1]]
        if target_piece == 'E':
            return True
        new_grid = [x[:] for x in grid] # Copy the grid
        new_grid[move[0]][move[1]] = 'S'
        if can_win(new_grid, target_piece):
            return True
    return False

results = []
c = int(input())
for case in range(1,c+1):
    if case > 1: input()
    grid = [list(input()) for i in range(8)]
    results.append(f'Case {case}: {"Yes" if can_win(grid) else "No"}')
print('\n'.join(results))