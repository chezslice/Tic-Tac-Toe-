"""
Tic Tac Toe Player
"""
import pygame
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # X get the first move, if the board is empty.
    if board == initial_state():
        return X

    # Counting function that individually count the number of input on screen.
    num_X = 0
    num_O = 0

    for row in board:
        num_X += row.count(X)
        num_O += row.count(O)

    if num_X > num_O:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Game of tic tac toe game logic code to check if there a empty space on board.
    move = set()

    # Interating thru the row and cells to check if the space is empty or not.
    for row in range(3):
        for cell in range(3):
            if board[row][cell] == EMPTY:
                move.add((row, cell))

    return move

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If the index is taken by another input return a exception.
    if action[0] not in range(0, 3) or action[1] not in range(0, 3) or board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action, please try again!")

    # Function that decides whose turn to make the move.
    board_state = copy.deepcopy(board)
    board_state[action[0]][action[1]] = player(board)
    return board_state

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Function to check if the game logic, if theres a row of input horiztonally.

    for plays in [X, O]:
        for row in range(0, 3):
            if all(board[row][col]==plays for col in range(0, 3)):
                return plays


    # Function to check if the game logic, if theres a row of input vertically.

    for col in range(0, 3):
            if all(board[row][col]==plays for row in range(0, 3)):
                return plays

    # Function to check if the game logic, if theres a row of input diagonals.

    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for diagonal in diagonals:
        if all(board[row][col]==plays for (row, col) in diagonal):
            return plays

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Function that helps logic to determine if the game is won or lost by whom X or O, by using True or false.
    if winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True

    # If all cells have been filed on screen return true.
    all_moves = [cell for row in board for cell in row]
    if not any(move==EMPTY for move in all_moves):
        return True

    # Otherwise return False.
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def min_value(board):

    # Function for Min value of current state.
    if terminal(board):
        return utility(board), None

    res = float('inf')
    action = None

    v = math.inf
    for move in actions(board):
        v = min(v, max_value(result(board, move)))
    return v

def max_value(board):

    # Function for Max_input of the current state.
    if terminal(board):
        return utility(board), None


    v = -math.inf
    for move in actions(board):
        v = max(v, min_value(result(board, move)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if termial(board):
        return None

    # Function to determine the input for the current player.
    # Calling upon function defining above max_value and min_value to help.
    if player(board) == X:
        best = -math.inf
        for move in actions(board):
            max_var = min_value(result(board, move))
            if max_var > best:
                best = max_var
                best_play = move

    elif player(board) == O:
        best = math.inf
        for move in actions(board):
            min_var = max_value(result(board, move))
            if min_var < best:
                best = min_var
                best_play = move
    return best_play

# Always test code!!
#print("Code Completed")
