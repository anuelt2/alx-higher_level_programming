#!/usr/bin/python3
from sys import argv, exit

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
if argv[1].isdigit():
    N = int(argv[1])
else:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)


def safe_square(chessboard, rank, file):
    """Checks for safe squares"""
    for sq in range(rank):
        if (chessboard[sq] == file or chessboard[sq] - sq == file - rank or
                chessboard[sq] + sq == file + rank):
            return False
    return True


def puzzle_sol(N):
    """Solves N queens puzzle"""
    def q_place(rank):
        """Recursive placement of queens"""
        if rank == N:
            solve = [[sq, chessboard[sq]] for sq in range(N)]
            solution.append(solve)
        else:
            for file in range(N):
                if safe_square(chessboard, rank, file):
                    chessboard[rank] = file
                    q_place(rank + 1)

    chessboard = [-1] * N
    solution = []
    q_place(0)
    return solution


solution = puzzle_sol(N)
for solve in solution:
    print(solve)
