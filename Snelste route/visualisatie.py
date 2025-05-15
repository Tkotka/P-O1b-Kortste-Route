import time

from Optimalisatie_startfile3 import *

def main():
    opl = [
        [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0), (2, 0), (2, 1), (2, 2), (3, 2), (2, 2), (1, 2), (1, 3), (1, 4),
         (2, 4), (2, 5), (1, 5), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0)],
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (2, 4), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2),
         (2, 2), (2, 1), (2, 0), (3, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 0)]]
    opl1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (2, 4), (1, 4), (1, 3), (1, 2), (2, 2), (3, 2), (2, 2), (2, 1), (2, 0), (3, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 0)]


    board_presentatie = initiate_board(4,6)

    putRed(board_presentatie,1,0)
    putRed(board_presentatie,3,1)
    putRed(board_presentatie,2,3)
    putRed(board_presentatie,3,3)

    putGreen(board_presentatie,2,0)
    putGreen(board_presentatie,3,0)
    putGreen(board_presentatie,2,1)
    putGreen(board_presentatie,3,2)
    putGreen(board_presentatie,2,4)
    putGreen(board_presentatie,0,5)

    for row in board_presentatie:
        print(row)

    for point in opl1:
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        board_point = board_presentatie[point[0]][point[1]]
        if board_point == "x":
            board_presentatie[point[0]][point[1]] = "X"
        elif board_point != "X":
            board_presentatie[point[0]][point[1]] = "x"
        for row in board_presentatie:
            print(row)
        time.sleep(1)

main()