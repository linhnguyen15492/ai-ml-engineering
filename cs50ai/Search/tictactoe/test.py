def print_board(board):
    for row in board:
        print(row)


def player(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    return 'X' if x_count <= o_count else 'O'


def actions(board):
    possible_moves = set()

    # Loop through each cell in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the cell is empty (assuming empty cells contain EMPTY or None)
            if board[i][j] is None:
                possible_moves.add((i, j))

    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    # Validate the move
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        raise ValueError("Move out of bounds")
    if board[i][j] is not None:  # Adjust EMPTY based on your implementation
        raise ValueError("Cell already occupied")

    # Create a deep copy of the board
    new_board = [row[:] for row in board]

    # Get the current player's mark
    current_player = player(board)

    # Make the move
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.

    Args:
        board: The game board (2D list/array)

    Returns:
        str: 'X' if X has won, 'O' if O has won, None if no winner
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:  # Adjust EMPTY as needed
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    Args:
        board: The game board (2D list/array)

    Returns:
        bool: True if game is over (winner or tie), False if game is still in progress
    """
    # Check if there's a winner
    if winner(board) is not None:
        return True

    # Check if board is full (no empty spaces left)
    for row in board:
        for cell in row:
            if cell is None:  # Adjust EMPTY based on your implementation
                return False

    # If no winner and no empty spaces, it's a tie
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    Args:
        board: The game board (2D list/array)

    Returns:
        int: 1 for X win, -1 for O win, 0 for tie or ongoing game
    """
    win = winner(board)

    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    Args:
        board: The game board (2D list/array)

    Returns:
        tuple: The optimal move (i, j) for the current player
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == 'X':
        # X is maximizing player
        best_value = float('-inf')
        best_move = None

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        # O is minimizing player
        best_value = float('inf')
        best_move = None

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move


def max_value(board):
    """Helper function for maximizing player"""

    if terminal(board):
        return utility(board)

    value = float('-inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))

        if value == 1:  # Nếu tìm thấy nước đi chiến thắng, dừng lại
            break

    return value


def min_value(board):
    """Helper function for minimizing player"""

    if terminal(board):
        return utility(board)

    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))

        if value == -1:  # Nếu tìm thấy nước đi thua, dừng lại
            break

    return value


def max_player(board):
    """Returns best value for maximizing player (X)"""
    if terminal(board):
        return utility(board)

    value = float('-inf')
    for move in actions(board):
        value = max(value, min_player(result(board, move)))

    return value


def min_player(board):
    """Returns best value for minimizing player (O)"""
    if terminal(board):
        return utility(board)

    value = float('inf')
    for move in actions(board):
        value = min(value, max_player(result(board, move)))

    return value


X = "X"
O = "O"
EMPTY = None

board = [[X, O, EMPTY],
         [X, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

print_board(board)

# while not terminal(board):
#     move = minimax(board)
#     board = result(board, move)
#     print_board(board)
#     print("Winner: ", winner(board), "\n")

optimal_move = minimax(board)
print(f"Optimal move for O: {optimal_move}")
