
# N = 8
# board = [-1] * N

# def safe(row, col):
#     for i in range(row):
#         if board[i] == col or abs(board[i] - col) == abs(i - row):
#             return False
#     return True

# def solve(row):
#     if row == N:
#         for i in range(N):
#             print(" _ " * board[i] + "Q" + " _ " * (N - board[i] - 1))
#         return True

#     for col in range(N):
#         if safe(row, col):
#             board[row] = col
#             if solve(row + 1):
#                 return True
#             board[row] = -1

#     return False

# solve(0)



# step 1 defining board
n=8
board=[-1]*n

def safe(row,col):
    for i in range(row):
        if (board[i]==col or abs(board[i]-col)==abs(i-row)):
            return False
    return True
def solve(row):

    if row==n:
        for i in range(n):
            print(" _ "*())
    for col in row:
        if safe(row,col):
            board[row]=col
            if (solve (row+1)):
                return True
            board[row] = -1

    return False
            