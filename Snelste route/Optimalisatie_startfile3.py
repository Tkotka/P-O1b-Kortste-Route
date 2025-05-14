#import time

TIMESTRAIGHT = 3  # tijd nodig om één vakje vooruit te rijden
TIMETURN = 4  # tijd nodig om binnen één vakje een kwart slag te draaien

ACCEPT = 'accept'
ABANDON = 'abandon'
CONTINUE = 'continue'
#LIST_CLASS = type([])
#SET_CLASS = type(set())
#TUPLE_CLASS = type((1, 2))
GREEN = "G"
RED = "R"


# INITIALISATIE

def initiate_board(nbRows, nbCols):
    """
    This function creates a new board with nbRows rows and nbCols columns.

    The board is a matrix (or a list of lists if you will) with each position being marked with " "
    to show it being empty.

    The function returns None in case of an invalid or non-positive input.
    :param nbRows: The amount of rows (integer)
    :param nbCols: The amount of columns (integer)
    :return: The board (a list of lists) or None if an error occurs
    """
    if type(nbRows) != int or type(nbCols) != int:  # input validation
        print("Invalid input")
        return # Identiek aan return None
    if nbRows < 1 or nbCols < 1:
        print(
            "Error: input must be strictly positive")  # attempting to make a board with <= 0 rows/columns is pointless
        return
    spelbord = [[" " for i in range(nbCols)] for j in range(nbRows)]
    # Exactly like this: if multiplying, a copy of the rows (i.e. lists) is made, which ruins
    # elementwise assignment. Iteration breaks this copying behaviour.
    return spelbord


def putGreen(board, row, col):
    """
    This function places a green tower on the (row,col) position on the board, represented by the "G" symbol.

    If the board is not a list, nothing happens.

    If row or col are not integers or out-of-bounds, the board is left unchanged.

    :param board: The board (a list of lists)
    :param row: The row-coordinate (integer)
    :param col: The col-coordinate (integer)
    :return: Technically nothing because it changes the board instead of making a copy
    """
    if type(board) != list:
        print("Board is not a list")
        return
    if type(row) != int or type(col) != int:
        print("Invalid pos values")
        return
    rows = len(board)
    cols = len(board[0])
    pos = (row, col)
    if not (0 <= row < rows and 0 <= col < cols): # python
        string = str(pos) + ": pos values out-of-bounds"
        print(string)
        return
    if board[row][col] == "G":
        print("Notice: this position", pos, "already is green")
    if board[row][col] == "R":
        print("Notice: this position", pos, "already is red")
    board[row][col] = "G"
    # PSA returning variables is unnecessary because LISTS ARE GODS


def putRed(board, row, col):
    """
    This function places a red tower on the (row,col) position on the board, represented by the "R" symbol.

    If the board is not a list, nothing happens.

    If row or y are not integers or out-of-bounds, the board is left unchanged.

    :param board: The board (a list of lists)
    :param row: The row-coordinate (integer)
    :param col: The y-coordinate (integer)
    :return: Technically nothing because it changes the board instead of making a copy
    """
    if type(board) != list:
        print("Board is not a list")
        return
    if type(row) != int or type(col) != int:
        print("Invalid pos values")
        return
    pos = (row, col)
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        string = str(pos) + ": pos values out-of-bounds"
        print(string)
        return
    if board[row][col] == "G":
        print("Notice: this position", pos, "already is green")
    if board[row][col] == "R":
        print("Notice: this position", pos, "already is red")
    board[row][col] = "R"


####################################################################################################################
############# HULP-FUNCTIES ######################################################################################
###################################################################################################################

def getGreens(board):
    """
    This function returns a set of all green positions.
    :param board: The board (list of lists)
    :return: All green positions (set of tuples)
    """
    if type(board) != list:
        print("Board is not a list")
        return
    greens = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "G":
                greens.add((row, col))
    return greens


def getReds(board):
    """
    This function returns a set of all red positions.
    :param board: The board (list of lists)
    :return: All red positions (set of tuples)
    """
    if type(board) != list:
        print("Board is not a list")
        return
    reds = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "R":
                reds.add((row, col))
    return reds


def getLegalNeighbours(board, pos):
    """
    This function returns a set of all neighbouring positions to which the car can move from the given position.
    Returns None if there are type errors or the position is out-of-bounds.
    Also, this function is apparently completely unused.

    :param board: The board (list of lists)
    :param pos: The examined position (tuple)
    :return: All legal neighbouring positions (set of tuples), or None if an error occurs.
    """
    if type(board) != list:
        print("Board is not a list")
        return
    if type(pos) != list and type(pos) != tuple:
        print("Pos is not a list, nor a tuple")
        return
    if not (0 <= pos[0] < len(board) or 0 <= pos[1] < len(board[0])):
        print(pos, "is out-of-bounds")
        return
    legal_neighbours = set()
    row, col = pos[0], pos[1]
    if board[row][col] == "R":
        print("Notice: this position", pos, "contains a red tower")
    for i1 in range(-1, 2, 1):  # Iterates over -1,0,1
        for i2 in range(-1, 2, 1):  # Iterates over -1,0,1 for each of the above
            if (i1 == 0 or i2 == 0) and i1 != i2:
                # When comparing the nine points around the given position including the position itself,
                # you can see that each possible legal neighbour has exactly one coordinate equal to that of the
                # given position. I.e. the only valid neighbours lie on, respectively,
                # the x- and y-axis of the given position.
                # If neither of the coordinates of the point are equal to the given coordinates,
                # it points to a position diagonal to the given, and if both are equal, it is the position itself.
                # Furthermore, each coordinate of the neighbour cannot differ more than 1 from the given coordinate
                # by definition.
                # Therefore: we iterate two variables over -1,0,1,
                # and only the differences where exactly one variable is zero are considered.
                row1, col1 = row + i1, col + i2
                if 0 <= row1 < len(board) and 0 <= col1 < len(board[row]) and board[row1][col1] != "R":
                    # a legal position cannot be outside the board or contain a red tower
                    legal_neighbours.add((row1, col1))
    return legal_neighbours


def calculateTime(route):
    """
    This function calculates the time needed to traverse a given route, utilising the constants TIMESTRAIGHT and TIMETURN.
    Assuming that first position has the correct rotation.
    :param route: The route (list of tuples)
    :return: Traversal time (integer) or None if there is a type error
    """
    # Assume that route is valid [lol nah, i like input validation]
    if type(route) != list:
        print("Route is not a list")
        return
    for point in route:
        if type(point) != tuple:
            print(point, "is not a tuple")
            return
    time = 0
    for n_waypoint in range(len(route)):
        # n-waypoint gives which waypoint (i.e. first, 2nd, ...) the car will move to.
        if n_waypoint == 0:
            pass  # First waypoint irrelevant for calculation: the car is already here
        elif n_waypoint == 1:
            time += TIMESTRAIGHT  # Assume car rotated correctly for first movement
        else:
            new_waypoint = route[n_waypoint]  # this is the waypoint the car will move to
            current_waypoint = route[n_waypoint - 1]  # waypoint where the car currently is
            old_waypoint = route[n_waypoint - 2]  # waypoint where the car came from
            if new_waypoint == old_waypoint:  # car must do a U-turn to get where it was
                time += (TIMETURN * 2 + TIMESTRAIGHT)  # rotate twice for a U-turn
            else:
                difference_nc = tuple_diff2(current_waypoint, new_waypoint)  # Difference of new to current
                difference_co = tuple_diff2(old_waypoint, current_waypoint)  # Difference of current to old
                if difference_nc == difference_co:  # If difference is equal, then the car did not change direction
                    time += TIMESTRAIGHT
                else:  # If neither of the previous is true, then the car must turn
                    time += (
                                TIMETURN + TIMESTRAIGHT)  # Assume that car can rotate both left and right and that the time to do this is equal
    return time


def check_bounds(board, pos):
    """
    Checks whether a given position is on the board (i.e. not out-of-bounds).
    :param board: The board (list of lists)
    :param pos: The position (tuple)
    :return: True if inside bounds, False otherwise
    """
    if type(board) != list:
        print("Board is not a list")
        return
    if type(pos) != list and type(pos) != tuple:
        print(pos, "is not a list or tuple")
        return
    row, col = pos[0], pos[1]
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        return True
    else:
        # print(pos,"is out-of-bounds")
        return False


def tuple_diff2(begin, end):
    """
    Gives the difference of two tuples.
    Note: the tuples must be 2 in length and the equation is end - begin.
    :param begin: Tuple 1
    :param end: Tuple 2
    :return: Tuple containing the difference of begin and end (or None if an error occurs)
    """
    if type(begin) != tuple or type(end) != tuple:
        print("At least one of the inputs is not a tuple")
        return
    if not (len(begin) == len(end) == 2):
        print("Incompatible dimensions, both tuples must be 2 in length")
        return
    x1, y1 = begin[0], begin[1]
    x2, y2 = end[0], end[1]
    difference = (x2 - x1, y2 - y1)
    return difference


def makeInstructionfile(route, board):
    """
        This function generates a .txt file containing the given route.

        Each row of the file has the format: row, col, True/False  |
        row is the row number, col is the column number, True/False indicates whether there is a green tower needing pickup

        Note: if a position with a green tower is visited multiple times, only the first time has a True.

        Does nothing if type-error

        Assume that route is valid otherwise.
    :param board: The board (list of lists
    :param route: The route (list of tuples)
    :return: Technically nothing, it writes a separate file
    """
    if type(route) != list:
        print("Route is not a list")
        return
    for point in route:
        if type(point) != tuple:
            print(point, "is not a tuple")
            return
    file = open('instructions.txt', 'w')  # creates a file. 'w' overwrites if already exists
    picked_up_pos = set()
    for pos in route:
        pick = "False"
        if board[pos[0]][pos[1]] == "G" and pos not in picked_up_pos:
            pick = "True"
            picked_up_pos.add(pos)
            # Noot: dit zorgt ervoor dat de schep niet nog een keer gaat werken als je
            # een tweede keer over de positie rijdt
        outputstring = str(pos[0]) + ", " + str(pos[1]) + ", " + pick + "\n"
        file.write(outputstring)
    file.close()


def examine(board, partial_solution, opl, finish):
    if len(opl) > 0:
        fastest_time = opl[0] # first element in opl is always the time
    else:
        fastest_time = -1 # i.e. does not exist
    last_pos = partial_solution[-1]
    if len(partial_solution) >= 3:
        if partial_solution[-3] == last_pos and len(getLegalNeighbours(board, partial_solution[-2])) != 1:
            # Assume that U-turns will only be executed is there is no other valid route
            return ABANDON
    if len(opl) != 0:
        if (calculateTime(partial_solution) > fastest_time > 0 # If fastest time exists and is shorter than the solution time
                or len(partial_solution) > 2 * len(board) * len(board[0])):
                # Assume that evaluating a solution that drove over the entire board twice is pointless
            return ABANDON
    if partial_solution.count(last_pos) > 3:
        # Assume that going over the same position four times is pointless
        return ABANDON
    if not (0 <= last_pos[0] < len(board) and 0 <= last_pos[1] < len(board[0])) or last_pos in getReds(board):
        # Illegal position
        # Only the last position in the partial solution needs evaluation: after all,
        # all other points have already been evaluated previously and have been found legal
        return ABANDON
    elif all(pos in partial_solution for pos in getGreens(board)) and finish == last_pos:
        # this cute little function all() returns true only if the entire iterable is true
        # All greens must be in the solution
        # Last position must be the finish
        return ACCEPT
    else:
        return CONTINUE


def extend(partial_solution):
    extended_solutions = []
    last_pos = partial_solution[-1]
    for i in [-1, 1]: # this is a list, not a range or whatever
        new_solution1 = partial_solution.copy()
        new_solution1.append((last_pos[0] - i, last_pos[1]))
        extended_solutions.append(new_solution1)
        new_solution2 = partial_solution.copy()
        new_solution2.append((last_pos[0], last_pos[1] - i))
        extended_solutions.append(new_solution2)
    return extended_solutions


def solve(board, opl, start=(0, 0), finish=(0, 0), partial_solution=None,teller=None):
    if teller is None:
        teller = 0
    if partial_solution is None:
        partial_solution = [start]
    exam = examine(board, partial_solution, opl, finish)
    if exam == ACCEPT:
        partial_time = calculateTime(partial_solution)
        if len(opl) == 0:
            fastest_time = partial_time
            print(partial_time) # purely informational
            opl.append(fastest_time) # first element in opl is the time
            opl.append(partial_solution)
        else:
            current_fastest_time = opl[0]
            if partial_time < current_fastest_time:
                opl.clear()
                fastest_time = partial_time
                print(partial_time)
                opl.append(fastest_time)
                opl.append(partial_solution)
            elif partial_time == current_fastest_time and partial_solution not in opl:
                print(partial_time)
                opl.append(partial_solution)
    else:
        if exam == CONTINUE:
            extended_solutions = extend(partial_solution)
            if len(opl) == 0:
                teller += 1
                print(teller)
            for solution in extended_solutions:
                solve(board, opl, start, finish, solution)


def fastest_route(board, start=(0, 0), finish=(0, 0)):
    opl = []
    solve(board, opl, start, finish)
    opl.pop(0)
    return opl
