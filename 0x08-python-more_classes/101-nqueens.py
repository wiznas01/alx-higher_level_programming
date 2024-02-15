#!/usr/bin/python3
import sys

def print_solution(board):
    """Print the N-Queens solution."""
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position."""
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, n):
    """Solve the N-Queens problem using backtracking."""
    if row == n:
        # If all queens are placed, print the solution
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen and move to the next row
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, n)
            # Backtrack: remove the queen to explore other possibilities
            board[row][col] = '.'

def nqueens(n):
    """Main function to solve the N-Queens problem."""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])

