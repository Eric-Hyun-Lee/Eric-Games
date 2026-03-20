ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = '.'

def create_board():
    """Creates an empty 7x6 Connect Four board using standard Python lists."""
    board = []
    # Create 6 rows
    for _ in range(ROW_COUNT):
        # Each row has 7 columns, initialized to '.'
        row = [EMPTY] * COLUMN_COUNT
        board.append(row)
    return board

def drop_piece(board, row, col, piece):
    """Places a player's piece into the specified row and column."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Checks if the top row of the selected column is empty."""
    # The top-most row is at index 0
    return board[0][col] == EMPTY

def get_next_open_row(board, col):
    """Finds the lowest empty row in the specified column."""
    # Iterate from the bottom row (index 5) up to the top (index 0)
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == EMPTY:
            return r
    return None

def winning_move(board, piece):
    """Checks all directions for four in a row using a helper function."""
    # Helper to check a line in any direction (dr=row_delta, dc=col_delta)
    def check_line(r, c, dr, dc, piece):
        for i in range(4):
            if not (0 <= r + i*dr < ROW_COUNT and 0 <= c + i*dc < COLUMN_COUNT and board[r + i*dr][c + i*dc] == piece):
                return False
        return True

    # Iterate through every cell and check all potential win directions (horizontal, vertical, diagonal)
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            # Check Horizontal (right)
            if c + 3 < COLUMN_COUNT and check_line(r, c, 0, 1, piece): 
                return True
            # Check Vertical (down)
            if r + 3 < ROW_COUNT and check_line(r, c, 1, 0, piece): 
                return True
            # Check Diagonal (down-right)
            if r + 3 < ROW_COUNT and c + 3 < COLUMN_COUNT and check_line(r, c, 1, 1, piece): 
                return True
            # Check Diagonal (up-right)
            if r - 3 >= 0 and c + 3 < COLUMN_COUNT and check_line(r, c, -1, 1, piece): 
                return True

    return False

def print_board(board):
    """Displays the board in the console (already bottom-up with standard lists)."""
    print("\n0 1 2 3 4 5 6") # Column headers
    for row in board:
        print(" ".join(row))
    print() # Add extra newline for spacing

# --- Main Game Loop ---

board = create_board()
game_over = False
turn = 0 

# Get player names at the start
player_x_name = input("Player X, enter your name: ")
player_o_name = input("Player O, enter your name: ")
players = [(player_x_name, 'X'), (player_o_name, 'O')]

print_board(board)

while not game_over:
    current_player_name, current_piece = players[turn]
    
    col = int(input(str(current_player_name) +", you are" + str(current_piece) + ".What column do you want to play in? "))
    
    # Process valid move
    if 0 <= col <= 6 and is_valid_location(board, col):
        row = get_next_open_row(board, col)
        if row is not None:
            drop_piece(board, row, col, current_piece)
            
            # Check for win
            if winning_move(board, current_piece):
                print_board(board)
                print("Congratulations, " +str(current_player_name) + ", you won!")
                game_over = True
            
            # Check for draw (board is full)
            # Flatten the list of lists to check if any empty spaces remain
            if not any(EMPTY in row for row in board) and not game_over:
                 print_board(board)
                 print("The game is a draw!")
                 game_over = True

            # Switch turns
            turn = (turn + 1) % 2 
        else:
            print("Error: Could not find an open row.")
    else:
        print("Column is full or input is invalid (must be 0-6)! Try again.")
    
    # Only print the board again if the game is still active
    if not game_over:
        print_board(board)