# Chess Game

# Board representation using a 2D list
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

# Function to print the current board state
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Example move function (not complete, handles only pawn movement)
def move_piece(start, end):
    # Convert input coordinates to board indices
    start_row, start_col = start[0], start[1]
    end_row, end_col = end[0], end[1]

    # Get the piece at the start position
    piece = board[start_row][start_col]

    # Check if it's a valid pawn move (forward, no capture)
    if piece == 'P' and start_col == end_col and end_row == start_row + 1:
        # Move the piece
        board[end_row][end_col] = piece
        board[start_row][start_col] = '.'
        print('Moved pawn successfully!')
    else:
        print('Invalid move!')

# Main game loop
def play_chess():
    while True:
        print_board(board)
        start = input("Enter start position (e.g., a2): ")
        end = input("Enter end position (e.g., a4): ")
        move_piece(start, end)

# Start the game
play_chess()
