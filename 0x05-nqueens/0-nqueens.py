#!/usr/bin/env python3
""" r, print N must be a number,
        followed by a new line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module """
import sys


def nqueens(n: int):
    """
    backtracking
    """
    matrix = [[0 for x in range(n)] for y in range(n)]
    print(str(matrix))


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    nqueens(int(sys.argv[1]))
