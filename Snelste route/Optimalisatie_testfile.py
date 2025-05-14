# importeer hier je oplossingenbestand

from Optimalisatie_startfile import *

###################################################################################################################
############# TESTEN ##############################################################################################
###################################################################################################################

def test_initiate_board():
    juist = 0
    totaal = 0

    board = initiate_board(0,4)
    totaal+=1
    if board is None:
        juist += 1
    else:
        print("Fout: initiate_board(0,4) geeft geen None-object terug.")


    board = initiate_board(5, -3)
    totaal += 1
    if board is None:
        juist += 1
    else:
        print("Fout: initiate_board(5,-3) geeft geen None-object terug.")

    board = initiate_board(4, 6)
    totaal += 1
    if len(board) == 4 and len(board[0])==6:
        juist += 1
    else:
        print("Fout: initiate_board(4,6) geeft geen matrix met 4 rijen en 6 kolommen.")

    totaal += 1
    leeg = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != " ":
                leeg = False
    if leeg:
        juist += 1
    else:
        print("Fout: initiate_board(4,6) geeft een bord waarvan niet alle elementen gelijk zijn aan een lege spatie.")

    print("Testen initiate_board(): ",juist,"/",totaal)

def test_putGreen():

    juist = 0
    totaal = 0

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    board = putGreen(board,2,1)
    totaal +=1
    if board[2][1] == "G":
        juist +=1
    else:
        print("Fout: putGreen(board,2,1) geeft geen bord met letter G op rij 2 en kolom1.")

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board = putGreen(board, -2, 1)
    totaal += 1
    test = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != " ":
                test = False
    if test:
        juist += 1
    else:
        print("Fout: putGreen(board,-2,1) moet het bord ongewijzigd laten.")

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board = putGreen(board, 2, -4)
    totaal += 1
    test = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != " ":
                test = False
    if test:
        juist += 1
    else:
        print("Fout: putGreen(board,2,-4) moet het bord ongewijzigd laten.")

    print("Testen putGreen(): ", juist, "/", totaal)


def test_putRed():

    juist = 0
    totaal = 0

    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    board = putRed(board,2,1)
    totaal +=1
    if board[2][1] == "R":
        juist +=1
    else:
        print("Fout: putRed(board,2,1) geeft geen bord met letter R op rij 2 en kolom1.")

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board = putRed(board, -2, 1)
    totaal += 1
    test = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != " ":
                test = False
    if test:
        juist += 1
    else:
        print("Fout: putRed(board,-2,1) moet het bord ongewijzigd laten.")

    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    board = putRed(board, 2, -4)
    totaal += 1
    test = True
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != " ":
                test = False
    if test:
        juist += 1
    else:
        print("Fout: putRed(board,2,-4) moet het bord ongewijzigd laten.")

    print("Testen putRed(): ", juist, "/", totaal)

def test_getGreens():
    juist = 0
    totaal = 0
    board = initiate_board(4,6)
    putGreen(board,1,2)
    putGreen(board,2,3)
    putGreen(board,3,1)
    putRed(board,2,4)
    allGreens = getGreens(board)
    totaal += 1
    if isinstance(allGreens,set):
        juist +=1
    else:
        print("Fout: getGreens(board) geeft geen set-object terug.")
    totaal +=1
    if len(allGreens) == 3:
        juist +=1
    else:
        print("Fout: getGreens(board) heeft niet het correct aantal elementen.")
    totaal+=1
    if allGreens == {(1,2),(2,3),(3,1)}:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = {(1,2),(2,3),(3,1)}, gegenereerde uitkomst = ",allGreens)
    print("Testen getGreens():",juist,"/",totaal)

def test_getReds():
    juist = 0
    totaal = 0
    board = initiate_board(4,6)
    putRed(board,1,2)
    putRed(board,2,3)
    putRed(board,3,1)
    putGreen(board,2,4)
    allReds = getReds(board)
    totaal += 1
    if isinstance(allReds,set):
        juist +=1
    else:
        print("Fout: getReds(board) geeft geen set-object terug.")
    totaal +=1
    if len(allReds) == 3:
        juist +=1
    else:
        print("Fout: getReds(board) heeft niet het correct aantal elementen.")
    totaal+=1
    if allReds == {(1,2),(2,3),(3,1)}:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = {(1,2),(2,3),(3,1)}, gegenereerde uitkomst = ",allReds)
    print("Testen getReds():",juist,"/",totaal)

def test_getLegalNeighbours():
    juist = 0
    totaal = 0
    board = initiate_board(5, 6)
    putGreen(board, 0, 2)
    putGreen(board, 3, 3)
    putGreen(board, 2, 5)
    putRed(board, 3, 1)
    test = getLegalNeighbours(board, (0, 0))
    totaal +=1
    if test == {(0, 1), (1, 0)}:
        juist +=1
    else:
        print("Fout: verwachte uitkomst = {(0, 1), (1, 0)}, gegenereerde uitkomst = ",test)
    test = getLegalNeighbours(board, (3, 2))
    totaal+=1
    if test == {(3,3),(2,2),(4, 2)}:
        juist +=1
    else:
        print("Fout: verwachte uitkomst = {(3,3),(2,2),(4, 2)}, gegenereerde uitkomst = ", test)
    test = getLegalNeighbours(board, (2,5))
    totaal += 1
    if test == {(2,4),(3,5),(1,5)}:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = {(2,4),(3,5),(1,5)}, gegenereerde uitkomst = ", test)
    print("Testen getLegalNeighbours(): ",juist,"/",totaal)

def test_calculateTime():
    juist = 0
    totaal = 0
    route1 = [(0, 0), (0, 1)]
    time1 = calculateTime(route1)
    totaal+=1
    if time1 == TIMESTRAIGHT:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = ",TIMESTRAIGHT, ", gegenereerde uitkommst : ",time1)
    route2 = [(0, 0), (0,1), (0, 0)]
    time2 = calculateTime(route2)
    totaal += 1
    if time2 == 2 * TIMESTRAIGHT + 2 * TIMETURN:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = ",2 * TIMESTRAIGHT + 2 * TIMETURN, ", gegenereerde uitkommst : ",time2)
    route3 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (1, 1), (0, 1), (0, 0)]
    time3 = calculateTime(route3)
    totaal += 1
    if time3 == 8 * TIMESTRAIGHT + 4 * TIMETURN:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = ", 8 * TIMESTRAIGHT + 4 * TIMETURN, ", gegenereerde uitkommst : ", time3)
    print("Testen calculateTime(): ",juist,"/",totaal)


def test_fastestRoute():
    juist = 0
    totaal = 0
    board = initiate_board(5, 6)
    putGreen(board, 0, 2)
    putGreen(board, 3, 3)
    putGreen(board, 2, 5)
    putRed(board, 4, 1)
    test1 = fastestRoute(board,(0,0),(0,5))
    totaal += 1
    if test1 == [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]:
        juist += 1
    else: print("Fout: verwachte uitkomst = ",[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)],", gegenereerde uitkomst : ",test1)
    test2 = fastestRoute(board, (4, 0), (4,2))
    totaal += 1
    if test2 == [(4,0),(3,0),(3,1),(3,2),(4,2)]:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = ", [(4,0),(3,0),(3,1),(3,2),(4,2)],
              ", gegenereerde uitkomst : ", test2)
    test3 = fastestRoute(board, (4, 0), (0,5))
    totaal += 1
    if test3 == [(4,0),(3,0),(2,0),(1,0),(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)]:
        juist += 1
    else:
        print("Fout: verwachte uitkomst = ", [(4,0),(3,0),(2,0),(1,0),(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)],
              ", gegenereerde uitkomst : ", test3)
    print("Testen fastestRoute(): ",juist,"/",totaal)


def test_collect():
    juist = 0
    totaal = 0

    board = initiate_board(3, 3)
    putGreen(board, 0, 1)
    putGreen(board, 2, 2)
    putGreen(board, 1, 0)
    putRed(board, 2, 0)
    test1 = collect(board, (0, 0), (0, 0))
    sol1 = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (1, 2), (1, 1), (1, 0), (0, 0)]
    totaal += 1
    if test1 == sol1 or test1 == sol1[::-1]:
        juist += 1
    else:
        print("Fout: collect - test 1")

    board = initiate_board(3, 3)
    putGreen(board, 0, 0)
    putGreen(board, 0, 2)
    test2 = collect(board, (0, 1), (0, 1))
    sol2 = [(0, 1), (0, 2), (0, 1), (0, 0), (0, 1)]
    totaal += 1
    if test2 == sol2 or test2 == sol2[::-1]:
        juist += 1
    else:
        print("Fout: collect - test 2")

    board = initiate_board(3, 4)
    putGreen(board, 0, 1)
    putGreen(board, 2, 2)
    putGreen(board, 2, 3)
    putRed(board, 2, 1)
    test3 = collect(board, (0, 0), (0, 0))
    sol3 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0)]
    totaal += 1
    if test3 == sol3 or test3 == sol3[::-1]:
        juist += 1
    else:
        print("Fout: collect - test 3")

    board = initiate_board(3, 4)
    putGreen(board, 0, 1)
    putGreen(board, 2, 2)
    putGreen(board, 2, 3)
    putGreen(board, 1, 0)
    putRed(board, 2, 1)
    putRed(board, 1, 2)
    test4 = collect(board, (0, 0), (0, 0))
    sol4 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (0, 0)]
    totaal += 1
    if test4 == sol4 or test4 == sol4[::-1]:
        juist += 1
    else:
        print("Fout: collect - test 4")

    board = initiate_board(5, 6)
    putGreen(board, 0, 1)
    putGreen(board, 4, 3)
    putGreen(board, 2, 5)
    putGreen(board, 3, 1)
    putRed(board, 2, 1)
    putRed(board, 4, 2)
    putRed(board, 1, 5)
    putRed(board, 0, 3)
    test5 = collect(board, (0, 0), (0, 0))
    sol5 = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (3, 5), (2, 5), (2, 4), (2, 3), (2, 2), (1, 2), (0, 2), (0, 1), (0,0)]
    totaal += 1
    if test5 == sol5 or test5 == sol5[::-1]:
        juist += 1
    else:
        print("Fout: collect - test 5")

    board = initiate_board(3, 3)
    putGreen(board, 0, 1)
    putGreen(board, 2, 1)
    putRed(board, 1, 0)
    putRed(board, 1, 1)
    putRed(board, 1, 2)
    test6 = collect(board, (0, 1), (0, 1))
    totaal += 1
    if test6 is None:
        juist += 1
    else:
        print("Fout: collect - test 6")
    print("Testen collect(): ",juist,"/", totaal)

def test_collect_opt():
    juist = 0
    totaal = 0

    board = initiate_board(3, 3)
    putGreen(board, 0, 0)
    putGreen(board, 0, 2)
    putGreen(board, 1, 2)
    putRed(board, 1, 1)
    test1 = collect_opt(board, (0, 1), (0, 1))
    sol1 = [(0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1)]
    totaal += 1
    if test1 == sol1 or test1 == sol1[::-1]:
        juist += 1
    else:
        print("Fout: collect_opt() test1")

    board = initiate_board(3, 4)
    putGreen(board, 0, 1)
    putGreen(board, 2, 2)
    putGreen(board, 2, 3)
    putGreen(board, 1, 0)
    putRed(board, 2, 1)
    putRed(board, 1, 2)
    test2 = collect_opt(board, (0, 0), (0, 0))
    sol2 = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0)]
    totaal += 1
    if test2 == sol2 or test2 == sol2[::-1]:
        juist += 1
    else:
        print("Fout: collect_opt() test2")

    board = initiate_board(3, 3)
    putGreen(board, 0, 1)
    putGreen(board, 2, 1)
    putRed(board, 1, 0)
    putRed(board, 1, 1)
    putRed(board, 1, 2)
    test3 = collect_opt(board, (0, 1), (0, 1))
    totaal+=1
    if test3 is None:
        juist += 1
    else:
        print("Fout: collect_opt() test3")

    board = initiate_board(3, 3)
    putGreen(board, 0, 0)
    putGreen(board, 0, 2)
    putGreen(board, 1, 2)
    putRed(board, 1, 1)
    test4 = collect_opt(board, (0, 1), (0, 1))
    sol4 = [(0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (0, 0), (0, 1)]
    totaal += 1
    if test4 == sol4 or test4 == sol4[::-1]:
        juist += 1
    else:
        print("Fout: collect_opt() test4")
    print()
    print("Optioneel:")
    print("Testen collect_opt(): ",juist,"/", totaal)

###################################################################################################################
############# MAIN ################################################################################################
###################################################################################################################


def main():
    test_initiate_board()
    #test_putGreen()
    #test_putRed()
    test_getGreens()
    test_getReds()
    test_getLegalNeighbours()
    test_calculateTime()
    test_fastestRoute()
    #test_collect()
    test_collect_opt()

main()