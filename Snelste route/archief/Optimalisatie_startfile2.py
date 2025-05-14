
TIMESTRAIGHT = 3    # tijd nodig om één vakje vooruit te rijden
TIMETURN = 4       # tijd nodig om binnen één vakje een kwart slag te draaien

ACCEPT = 'accept'
ABANDON = 'abandon'
CONTINUE = 'continue'
LIST_CLASS = type([])
SET_CLASS = type(set())
TUPLE_CLASS = type((1,2))
GREEN = "G"
RED = "R"

# INITIALISATIE

def initiate_board(nbRows,nbCols):
    """
    This function creates a new board with nbRows rows and nbCols columns.

    The board is a matrix (or a list of lists if you will) with each position being marked with " " to show it being empty

    The function returns None in case of an invalid or non-positive input.
    :param nbRows: The amount of rows (integer)
    :param nbCols: The amount of columns (integer)
    :return: The board (a list of lists) or None if an error occurs
    """
    try:
        nbRows,nbCols = int(nbRows),int(nbCols) # convert to integers
    except TypeError or ValueError: # input validation
        print("Invalid input")
        return None
    if nbRows < 1 or nbCols < 1:
        print("Error: input must be strictly positive") # attempting to make a board with <= 0 rows/columns is pointless
        return None
    spelbord = [[" " for i in range(nbCols)] for j in range(nbRows)]
    # Exactly like this: if multiplying, a copy of the rows (i.e. lists) is made, which ruins
    # elementwise assigment. Iteration breaks this copying behaviour.
    return spelbord

def putGreen(board,x,y):
    """
    This function places a green tower on the (x,y) position on the board, represented by the "G" symbol.

    If the board is not a list, nothing happens.

    If x or y are not integers or out-of-bounds, the board is left unchanged.

    :param board: The board (a list of lists)
    :param x: The x-coordinate (integer)
    :param y: The y-coordinate (integer)
    :return: Technically nothing because it changes the board instead of making a copy
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    try:
        x, y = int(x), int(y)
    except TypeError or ValueError:
        print("Invalid pos values")
        return
    rows = len(board)
    cols = len(board[0])
    pos = (x, y)
    if not (0 <= x < rows and 0 <= y < cols):
        string = str(pos) + ": pos values out-of-bounds"
        print(string)
        return
    if board[x][y] == "G":
        print("Notice: this position",pos, "already is green")
    if board[x][y] == "R":
        print("Notice: this position",pos, "already is red")
    board[x][y] = "G"
    # PSA returning variables is unnecessary because LISTS ARE GODS


def putRed(board, x, y):
    """
    This function places a red tower on the (x,y) position on the board, represented by the "R" symbol.

    If the board is not a list, nothing happens.

    If x or y are not integers or out-of-bounds, the board is left unchanged.

    :param board: The board (a list of lists)
    :param x: The x-coordinate (integer)
    :param y: The y-coordinate (integer)
    :return: Technically nothing because it changes the board instead of making a copy
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    try:
        x, y = int(x), int(y)
    except TypeError or ValueError:
        print("Invalid pos values")
        return
    pos = (x, y)
    if not (0 <= x < len(board) and 0 <= y < len(board[x])):
        string = str(pos) + ": pos values out-of-bounds"
        print(string)
        return
    if board[x][y] == "G":
        print("Notice: this position",pos, "already is green")
    if board[x][y] == "R":
        print("Notice: this position",pos, "already is red")
    board[x][y] = "R"


###################################################################################################################
############# HULP-FUNCTIES ######################################################################################
###################################################################################################################

def getGreens(board):
    """
    This function returns a set of all green positions.
    :param board: The board (list of lists)
    :return: All green positions (set of tuples)
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    greens = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "G":
                greens.add((row,col))
    return greens

def getReds(board):
    """
    This function returns a set of all red positions.
    :param board: The board (list of lists)
    :return: All red positions (set of tuples)
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    reds = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "R":
                reds.add((row,col))
    return reds


def getLegalNeighbours(board,pos):
    """
    This function returns a set of all neighbouring positions to which the car can move from the given position.
    Returns None if there are type errors or the position is out-of-bounds.
    Also, this function is apparently completely unused.

    :param board: The board (list of lists)
    :param pos: The examined position (tuple)
    :return: All legal neighbouring positions (set of tuples), or None if an error occurs.
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    if type(pos) != LIST_CLASS and type(pos) != TUPLE_CLASS:
        print("Pos is not a list, nor a tuple")
        return
    if not (0 <= pos[0] < len(board) or 0 <= pos[1] < len(board[pos[0]])):
        print(pos,"is out-of-bounds")
        return
    legal_neighbours = set()
    x,y = pos[0],pos[1]
    if board[x][y] == "R":
        print("Notice: this position",pos,"contains a red tower")
    for i1 in range(-1,2,1): # Iterates over -1,0,1
        for i2 in range(-1,2,1): # Iterates over -1,0,1 for each of the above
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
                row,col = x+i1,y+i2
                if 0 <= row < len(board) and 0 <= col < len(board[row]) and board[row][col] != "R":
                    legal_neighbours.add((row,col))
    return legal_neighbours

def calculateTime(route):
    """
    This function calculates the time needed to traverse a given route, utilising the constants TIMESTRAIGHT and TIMETURN.
    Assuming that first position has the correct rotation.
    :param route: The route (list of tuples)
    :return: Traversal time (integer) or None if there is a type error
    """
    # Assume that route is valid [lol nah, i like input validation]
    if type(route) != LIST_CLASS:
        print("Route is not a list")
        return
    for point in route:
        if type(point) != TUPLE_CLASS:
            print(point, "is not a tuple")
            return
    time = 0
    for n_waypoint in range(len(route)):
        # n-waypoint gives which waypoint (i.e. first, 2nd, ...) the car will move to.
        if n_waypoint == 0:
            pass # First waypoint irrelevant for calculation: the car is already here
        elif n_waypoint == 1:
            time += TIMESTRAIGHT # Assume car rotated correctly for first movement
        else:
            new_waypoint = route[n_waypoint] # this is the waypoint the car will move to
            current_waypoint = route[n_waypoint-1] # waypoint where the car currently is
            old_waypoint = route[n_waypoint-2] # waypoint where the car came from
            if new_waypoint == old_waypoint: # car must do a U-turn to get where it was
                time += (TIMETURN*2 + TIMESTRAIGHT) # rotate twice for a U-turn
            else:
                difference_nc = tuple_diff2(current_waypoint,new_waypoint) # Difference of new to current
                difference_co = tuple_diff2(old_waypoint,current_waypoint) # Difference of current to old
                if difference_nc == difference_co: # If difference is equal, then the car did not change direction
                    time += TIMESTRAIGHT
                else: # If neither of the previous is true, then the car must turn
                    time += (TIMETURN + TIMESTRAIGHT) # Assume that car can rotate both left and right and that the time to do this is equal
    return time

def check_bounds(board,pos):
    """
    Checks whether a given position is on the board (i.e. not out-of-bounds).
    :param board: The board (list of lists)
    :param pos: The position (tuple)
    :return: True if inside bounds, False otherwise
    """
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    if type(pos) != LIST_CLASS and type(pos) != TUPLE_CLASS:
        print(pos,"is not a list or tuple")
        return
    x,y = pos[0],pos[1]
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    else:
        #print(pos,"is out-of-bounds")
        return False


def tuple_diff2(begin,end):
    """
    Gives the difference of two tuples.
    Note: the tuples must be 2 in length and the equation is end - begin.
    :param begin: Tuple 1
    :param end: Tuple 2
    :return: Tuple containing the difference of begin and end (or None if an error occurs)
    """
    if type(begin) != TUPLE_CLASS or type(end) != TUPLE_CLASS:
        print("At least one of the inputs is not a tuple")
        return
    if not (len(begin) == len(end) == 2):
        print("Incompatible dimensions, both tuples must be 2 in length")
        return
    x1,y1 = begin[0],begin[1]
    x2,y2 = end[0],end[1]
    difference = (x2-x1,y2-y1)
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
    if type(route) != LIST_CLASS:
        print("Route is not a list")
        return
    for point in route:
        if type(point) != TUPLE_CLASS:
            print(point, "is not a tuple")
            return
    file = open('../instructions.txt', 'w') # creates a file. 'w' overwrites if already exists
    picked_up_pos = set()
    for pos in route:
        pick = "False"
        if board[pos[0]][pos[1]] == "G" and pos not in picked_up_pos:
            pick = "True"
            picked_up_pos.add((pos[0],pos[1]))
            # Noot: dit zorgt ervoor dat de schep niet nog een keer gaat werken als je
            # een tweede keer over de positie rijdt
        outputstring = str(pos[0])+", "+str(pos[1]) +", " + pick + "\n"
        file.write(outputstring)
    file.close()


###################################################################################################################
############# BACKTRACKING - sub-optimaal #########################################################################
###################################################################################################################

"""
In deze variant mag je gebruik maken van de functie 'fastestRoute' die alvast de snelste
route tussen twee willekeurige posities op het bord bepaalt.
Gebruik makend van deze functie kan je zelf de snelste route bepalen waarmee alle groene schijfjes
kunnen opgepikt worden door deze route te interpreteren als een aaneenschakeling van snelste routes tussen twee
groene schijfjes onderling.
Let wel, dit algoritme geeft niet altijd de juiste oplossing voor de 'totale' snelste route, omdat het geen rekening
houdt met de eventuele draaitijden op de vakjes waar groene schijfjes liggen.
"""

def examine_help(board,partial_solution,finish):
    """
    Examine-function for the fastestRoute-function.
    :param board: The board (a list of lists)
    :param partial_solution: a partial route, must be a list of tuples
    :param finish: The desired finish position, a tuple
    :return: ACCEPT if this is a valid solution (i.e. the finish has been reached);
             ABANDON if the solution is invalid (ex. meets a red or goes out-of-bounds);
             CONTINUE otherwise (solution might be valid, will be extended later)
    """

    pos = partial_solution[-1] # Last position
    if not check_bounds(board,pos): # Out-of-bounds
        return ABANDON
    board_pos = board[pos[0]][pos[1]]
    #if all_solutions != [] and len(partial_solution) > len(all_solutions[0]):
        #return ABANDON
    # suppressed because a route with fewer points might not necessarily be shorter in terms of time
    if pos == finish:
        return ACCEPT
    elif board_pos == RED:
        return ABANDON
    else:
        return CONTINUE

def extend_help(partial_solution):
    """
    Extend-function for the fastestRoute function
    :param partial_solution: a partial route, must be a list of tuples
    :return: a list of up to four extended solutions, each of which is a list of tuples
    """
    pos = partial_solution[-1] # Last position i.e. the current position of the car
    extended_solutions = []
    for x in [-1,1]: # PS this is a list, containing -1 and 1
        solution = partial_solution.copy() # must be copied to break that annoying reference behaviour from the beginning
        new_position = (pos[0] + x,pos[1])
        if new_position not in solution:
            # the fastest route from point A to point B [WITHOUT ANY REQUIRED POINTS IN THE MIDDLE]
            # will never cross a position twice
            solution.append(new_position)
            extended_solutions.append(solution)
    for y in [-1,1]:
        solution = partial_solution.copy()
        new_position = (pos[0],pos[1]+y)
        if new_position not in solution:
            solution.append(new_position)
            extended_solutions.append(solution)
    return extended_solutions

def solve_help(board,partial_solution,all_solutions,finish):
    """
    Solve-function for the fastestRoute function.
    :param board: The board (a list of lists)
    :param partial_solution: A partial route, a list of tuples;
                             Also: the initial route must be a list containing the start position in tuple-form (integrated in fastestRoute)
    :param all_solutions: The list in which to dump valid solutions
    :param finish: The desired finish position
    :return: Technically nothing but all_solutions will be adjusted (hopefully, otherwise something broke or the desired route itself is invalid)
    """
    # PS gives all solutions
    exam = examine_help(board, partial_solution, finish)
    if exam == ACCEPT:
        all_solutions.append(partial_solution)
    else:
        if exam == CONTINUE:
            extended_partial_solutions = extend_help(partial_solution)
            for extended in extended_partial_solutions:
                solve_help(board, extended, all_solutions, finish)
        # PS if exam is abandoned, the next solve loop will not happen and the branch becomes irrelevant
def fastestRoute(board, start, finish):
    """
    De functie geeft de snelste route terug om van de positie 'start' naar de positie 'finish' te rijden op
    het gegeven bord. De route vermijdt daarbij de posities waar rode schijfjes aanwezig zijn (al geintegreerd in examine_help).

    Je mag ervan uitgaan dat start en finish beiden tupels zijn met een x- en een y-coördinaat die de dimensies
    van het gegeven bord respecteren.

    Dit zal Prof. Holvoet samen met jullie bekijken in de les in semesterweek 9.

    :param board: The board (a list of lists)
    :param start: The start position (must be a tuple)
    :param finish: The finish position (must be a tuple)
    :return: A list containing the fastest routes as lists of tuples (time is not returned to avoid death)
    """
    # we could have fun and add input validation
    if type(board) != LIST_CLASS:
        print("Board is not a list")
        return
    if type(start) != TUPLE_CLASS or type(finish) != TUPLE_CLASS:
        print("Start or finish isn't a tuple")
        return
    solution_list = []
    initial_solution = [start] # List containing a single tuple
    solve_help(board,initial_solution,solution_list,finish) # Gives ALL solutions
    fastest_routes = [solution_list[0]] # Assume that first route is fastest
    fastest_time = calculateTime(fastest_routes[0]) # Calculate time necessary for constants
    for route in solution_list: # Iterate over each solution route
        if route not in fastest_routes and calculateTime(route) < fastest_time:
            fastest_routes = [route]
            fastest_time = calculateTime(route)
            # If route is faster, reset fastest route list, add the new route and set the new fastest time
        elif route not in fastest_routes and calculateTime(route) == fastest_time:
            fastest_routes.append(route)
            # If route is equally fast, add the route to the list
    return fastest_routes

def examine(board,partial_solution,finish,fastest_time=None):
    """
    Examine-function for the collect-function.
    :param board: The board (list of lists)
    :param partial_solution: The partial route to be examined (list of tuples)
    :param finish: The finish position (tuple)
    :return: ACCEPT if the finish is the last point of the partial solution
             and the route contains all greens;
             CONTINUE otherwise
    """
    greens = getGreens(board)
    condition_greens = False
    check_greens = True
    for tower in greens:
        if tower not in partial_solution:
            check_greens = False
    if check_greens:
        condition_greens = True
    time = calculateTime(partial_solution)
    if fastest_time is not None:
        if time > fastest_time:
            return ABANDON
    elif partial_solution[-1] == finish and condition_greens:
        return ACCEPT
    else:
        return CONTINUE

def extend(board,partial_solution,finish):
    """
    Extend-function for the collect-function.
    Notes on how this works:
    If not all greens have been collected, it grabs all uncollected greens, gets all the fastest routes to all these greens individually, and gives all extended solutions based on all these routes.
    Otherwise, it gets all routes to finish.
    :param board: The board (a list of lists)
    :param partial_solution: The partial route (list of tuples)
    :param finish: The final finish position
    :return: A list of extended partial solutions (list of lists of tuples)
    """
    greens = getGreens(board)
    pos = partial_solution[-1]
    actual_greens = set()
    extended_solutions = []
    for gpos in greens:
        if gpos not in partial_solution:
            actual_greens.add(gpos)
    if actual_greens != set():
        for gpos in actual_greens:
            potential_routes = fastestRoute(board,pos,gpos)
            for route in potential_routes:
                rogue_green = False
                for pos1 in route[1:len(route)-1]:
                    if pos1 in actual_greens:
                        rogue_green = True
                if not rogue_green:
                    extended_route = partial_solution.copy()
                    for pos1 in route[1:len(route)]:
                        extended_route.append(pos1)
                    extended_solutions.append(extended_route)
    else:
        potential_routes = fastestRoute(board,pos,finish)
        for route in potential_routes:
            extended_route = partial_solution.copy()
            for pos1 in extended_route[1:len(route)]:
                extended_route.append(pos1)
            extended_solutions.append(extended_route)
    return extended_solutions


def solve(board,partial_solution,all_solutions,finish,fastest_time):
    """
        solve-functie voor de 'collect'-backtracking.
    """
    if all_solutions != [] and fastest_time is None:
        fastest_time = calculateTime(all_solutions[0])
    exam = examine(board, partial_solution, finish, fastest_time)
    if exam == ACCEPT:
        all_solutions.append(partial_solution)
    else:
        if exam == CONTINUE:
            extended_partial_solutions = extend(board,partial_solution,finish)
            for extended in extended_partial_solutions:
                solve(board, extended, all_solutions, finish, fastest_time)


def collect(board,start,finish):
    """
        Deze functie geeft de snelste route terug om van de positie 'start' naar de positie 'finish' te rijden op
        het gegeven bord, waarbij de posities van alle groene schijfjes onderweg worden aangedaan door de route.

        Deze functie maakt gebruik van de hulpfunctie 'fastestRoute' en berekent de snelste route als een
        aaneenschakeling van snelste routes tussen twee groene schijfjes onderling.

        De functie houdt geen rekening met eventuele draaitijden die het wagentje nodig heeft om op de plek van het
        groene schijfje zelf eventueel van richting te veranderen.
    """
    # I think the trick is to get the start position, extend to ALL the greens, calculate fastest route,
    # repeat until all greens are collected, then do the same to go from last green to finish ig,
    # then we will have a bunch of routes for which to calculate the fastest
    # and then if we have time we can integrate an additional function that also calculates turns.
    solution_list = []
    initial_solution = [start]
    fastest_time = None
    solve(board,initial_solution,solution_list,finish,fastest_time)
    fastest_routes = [solution_list[0]]
    fastest_time = calculateTime(fastest_routes[0])
    for route in solution_list:
        if route not in fastest_routes and calculateTime(route) < fastest_time:
            fastest_routes = [route]
            fastest_time = calculateTime(route)
        elif route not in fastest_routes and calculateTime(route) == fastest_time:
            fastest_routes.append(route)
    return fastest_routes


###################################################################################################################
############# BACKTRACKING - optimaal #############################################################################
###################################################################################################################

# kies zelf of je hier verder in gaat en een meer optimale oplossing probeert te schrijven die ook rekening houdt
# met de draaitijden van het wagentje op de posities van de groene schijfjes zelf.
def collect_opt(board, start, finish):
    """
            Deze functie geeft de snelste route terug om van de positie 'start' naar de positie 'finish' te rijden op
            het gegeven bord, waarbij de posities van alle groene schijfjes onderweg worden aangedaan door de route.

            De functie houdt daarbij rekening met eventuele draaitijden die het wagentje nodig heeft om op de plek van de
            groene schijfjes zelf eventueel van richting te veranderen.
        """
    pass


