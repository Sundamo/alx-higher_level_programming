#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys

def print_solution(queens):
    for row in queens:
        print(" ".join(row))
    print()

def is_safe(queens, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if queens[i][col] == 'Q':
            return False

    # Check if there is a queen in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if queens[i][j] == 'Q':
            return False

    # Check if there is a queen in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if queens[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    queens = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(queens, 0, n, solutions)
    return solutions

def solve_nqueens_util(queens, row, n, solutions):
    if row == n:
        solutions.append(["".join(row) for row in queens])
        return

    for col in range(n):
        if is_safe(queens, row, col, n):
            queens[row][col] = 'Q'
            solve_nqueens_util(queens, row + 1, n, solutions)
            queens[row][col] = '.'

def main():
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

    solutions = solve_nqueens(N)

    for solution in solutions:
        print_solution(solution)

if __name__ == "__main__":
    main()
