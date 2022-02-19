#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
    else:
        Min = 9999999
        for row in board:
            for cell in row:
                if cell=='d':
                    distance = abs(posr-board.index(row)) + abs(posc-                         row.index(cell))
                    if Min > distance:
                        Min = distance
                        r = board.index(row)
                        c = row.index(cell)
        if r > posr:
            print("DOWN")
        elif r < posr:
            print("UP")
        elif c > posc:
            print("RIGHT")
        else:
            print("LEFT")
                    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
