import time
from random import randint

from Optimalisatie import *


def random_red_green_arrangement(board,nbGreens,nbReds):
    placed_reds = set()
    placed_greens = set()
    while len(placed_reds) < nbReds:
        row = randint(0,len(board)-1)
        col = randint(0,len(board[0])-1)
        if board[row][col] == " " and not (row == 0 and col == 0):
            board[row][col] = "R"
            placed_reds.add((row,col))
    while len(placed_greens) < nbGreens:
        row = randint(0, len(board) - 1)
        col = randint(0, len(board[0]) - 1)
        #pot_green_pos = board[row][col]
        if board[row][col] == " " and not (row == 0 and col == 0):
            board[row][col] = "G"
            placed_greens.add((row, col))




#putGreen(bord,1,3)
#putRed(bord,1,1)
#putRed(bord,2,4)
#putGreen(bord,3,5)
#putGreen(bord,2,2)
#putRed(bord,0,2)
#putRed(bord,3,4)
#putGreen(bord,3,0)
#putGreen(bord,0,5)
#putGreen(bord,3,3)


def main():
    board1 = initiate_board(4,6)
    random_red_green_arrangement(board1,6,4)
    for row in board1:
        print(row)
    input("Ready?")
    t1 = time.perf_counter()
    route = fastest_route(board1,(0,0),(0,0))
    t2 = time.perf_counter()
    print("Route time: ", calculateTime(route[0]))

    for indiv_route in route:
        string = str(indiv_route) + "; Solution length: " + str(len(indiv_route))
        print(string)
    print("Time elapsed:", t2-t1)
    for row in board1:
        print(row)

# for some reason sometimes this is solved in 0.2 seconds and sometimes it takes like 15 minutes (689 seconds)
# (imma leave it rn to actually time it)

def main2():
    board2 = initiate_board(4,6)
    putGreen(board2,3,0)
    for j in range(4):
        putGreen(board2,j,4)
    for i in range(4):
        putRed(board2,i,1)
    route = fastest_route(board2,(0,0),(0,0))
    print(route)

def main3():
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

    input("Continue? ")

    route = fastest_route(board_presentatie)
    for opl in route:
        print(opl)

main3()