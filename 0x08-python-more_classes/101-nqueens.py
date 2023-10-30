#!/usr/bin/python3
"""
This program solves the N queens problem.
"""

import sys


def solve(board, col):
    """
    Recursive function to solve the N-queens problem using backtracking
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if check(board, i, col):
            board[i][col] = 1
            solve(board, col + 1)
            board[i][col] = 0


def check(board, row, col):
    """
    Check if a queen can be placed at the given position (row, col)
    without attacking any other queens on the board
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

board = [[0] * N for _ in range(N)]

solutions = []

solve(board, 0)

for solution in solutions:
    print(solution)
