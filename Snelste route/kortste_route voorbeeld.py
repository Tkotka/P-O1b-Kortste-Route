import time

ACCEPT = 'accept'
ABANDON = 'abandon'
CONTINUE = 'continue'
VRIJ = 'o'
ROOD = 'x'
GROEN = 'g'


def examine_help(board, partial_solution, opl, finish):
    if len(opl) != 0:
        snelste_tijd = opl[0]
    else:
        snelste_tijd = -1
    pos = partial_solution[-1]
    if len(partial_solution) >= 3:
        if partial_solution[-3] == pos and len(get_legal_neighbours(board, partial_solution[-2])) != 1: #alleen terug achteruit mag als er geen andere oplossing was
            return ABANDON
    if len(opl) != 0:
        if calculate_time(partial_solution) > snelste_tijd and snelste_tijd > 0 or len(partial_solution) > 2*len(board)*len(board[0]):
            return ABANDON
    if partial_solution.count(pos) > 3: #niet meer dan 2 keer zelfde plek
        return ABANDON
    if all(plek in partial_solution for plek in GROEN_plekken) and finish == pos: #alle groene gezien en rond
        return ACCEPT
    elif not (0 <= pos[0] <= len(board)- 1 and 0 <= pos[1] <= len(board[0]) - 1) or board[pos[0]][pos[1]] == ROOD: #niet binnen bord of op rood
        return ABANDON
    else:
        return CONTINUE

def extend_help(partial_solution):
    uitgebreid = []
    pos = (partial_solution[-1])
    for x in [-1, 1]:
        nieuwe = partial_solution.copy()
        nieuwe.append((pos[0] + x, pos[1]))
        uitgebreid.append(nieuwe)
    for y in [-1, 1]:
        nieuwe = partial_solution.copy()
        nieuwe.append((pos[0], pos[1] + y))
        uitgebreid.append(nieuwe)
    return uitgebreid

def solve_help(board, start, opl,partial_solution = [], teller = []):
    teller.append('i')
    #print(partial_solution)
    if len(partial_solution) == 0:
        partial_solution.append(start)
    exam = examine_help(board, partial_solution, opl, start)
    if exam == ACCEPT:
        tijd_partiele = calculate_time(partial_solution)
        if len(opl) != 0:
            tijd_totnutoe_snelste = opl[0]
            #print('partiele', tijd_partiele)
            #print('totnu snelste', tijd_totnutoe_snelste)
            if tijd_totnutoe_snelste > tijd_partiele:
                opl.clear()
                print(tijd_partiele)
                snelste_tijd = tijd_partiele
                opl.append(snelste_tijd)
                opl.append(partial_solution)

            elif tijd_partiele == tijd_totnutoe_snelste and partial_solution not in opl:
                opl.append(partial_solution)
        else:
            snelste_tijd = tijd_partiele
            opl.append(snelste_tijd)
            opl.append(partial_solution)
    elif exam == CONTINUE:
        uitgebreid = extend_help(partial_solution)
        for nieuwe_part in uitgebreid:
            solve_help(board, start, opl, nieuwe_part, teller)
def fastestRoute(board, start):
    opl = []
    teller = []
    solve_help(board, start, opl, [], teller)
    print('lengte teller', len(teller))
    opl.pop(0)
    return opl


def get_legal_neighbours(board, pos):
    legal_neighbours = set()
    for i in [-1, 1]:
        if len(board) > pos[0]+i >= 0:
            if board[pos[0]+i][pos[1]] == VRIJ or board[pos[0]+i][pos[1]] == GROEN:
                legal_neighbours.add((pos[0]+i, pos[1]))
        if len(board[0]) > pos[1] + i >= 0:
            if board[pos[0]][pos[1]+i] == VRIJ or board[pos[0]][pos[1]+i] == GROEN:
                legal_neighbours.add((pos[0], pos[1] + i))
    return legal_neighbours


def links_rechts_vooruit_omzetten(route):
    if route[0][0] < route[1][0]:
        route_met_richtingen = ['VERTICALE START']
    else:
        route_met_richtingen = ['HORIZONTALE START']
    for i in range(1, len(route)):
        if i == len(route)-1:
            route_met_richtingen.append('klaar')
        elif route[i-1] == route[i+1]:
            route_met_richtingen.append('omdraaien')
        elif route[i-1][0] == route[i][0] == route[i+1][0] or route[i-1][1] == route[i][1] == route[i+1][1]:
                route_met_richtingen.append('vooruit')
        elif route[i-1][0] == route[i][0] < route[i+1][0]:
            if route[i - 1][1] < route[i][1]:
                route_met_richtingen.append('rechts')
            else:
                route_met_richtingen.append('links')
        elif route[i-1][0] == route[i][0] > route[i+1][0]:
            if route[i - 1][1] < route[i][1]:
                route_met_richtingen.append('links')
            else:
                route_met_richtingen.append('rechts')
        elif route[i-1][1] == route[i][1] < route[i+1][1]:
            if route[i - 1][0] < route[i][0]:
                route_met_richtingen.append('links')
            else:
                route_met_richtingen.append('rechts')
        elif route[i-1][1] == route[i][1] > route[i+1][1]:
            if route[i - 1][0] < route[i][0]:
                route_met_richtingen.append('rechts')
            else:
                route_met_richtingen.append('links')
    return route_met_richtingen

def calculate_time(route):
    richtingen = links_rechts_vooruit_omzetten(route)
    tijd = 0
    for richting in richtingen:
        if richting == 'HORIZONTALE START' or richting == 'VERTICALE START':
            tijd += TIMESTRAIGHT
        elif richting == 'vooruit':
            tijd += TIMESTRAIGHT
        elif richting == 'klaar':
            tijd += 0
        elif richting == 'omdraaien':
            tijd += 2 * TIMETURN + TIMESTRAIGHT
        else:
            tijd += TIMESTRAIGHT + TIMETURN
    return tijd

def lijst_voor_instructiefile(snelste_route):
    richtingen_snelste = links_rechts_vooruit_omzetten(snelste_route)
    output_lijst = []
    for i in range(len(snelste_route)):
        output_lijst.append((snelste_route[i][0], snelste_route[i][1], richtingen_snelste[i], snelste_route[i] in GROEN_plekken))

    return output_lijst
def write_instructionfile(snelste_route):
        file = open('instructions.txt', 'w')
        for pos in snelste_route:
            outputstring = str(pos[0]) + "," + str(pos[1]) + ',' + str(pos[2]) + "," + str(pos[3]) + "\n"
            file.write(outputstring)
        file.close()

#board = [
    #    [VRIJ, ROOD, GROEN, ROOD, ROOD, GROEN],
   #     [VRIJ, ROOD,VRIJ,  ROOD, VRIJ, VRIJ],
  #      [VRIJ, VRIJ, VRIJ, VRIJ, VRIJ, VRIJ],
#        [VRIJ, ROOD, GROEN, ROOD, VRIJ, GROEN]
 #        ] #deze moet 4 keer door zelfde punt dus aanpassen in examine, maar dit soort verldopstelling is niet te maken met 4 rode pucks
board = [
        [VRIJ, GROEN, ROOD, VRIJ, VRIJ, GROEN],
        [VRIJ, VRIJ,ROOD,  VRIJ, ROOD, VRIJ],
        [VRIJ, VRIJ, VRIJ, VRIJ, VRIJ, VRIJ],
        [GROEN, VRIJ, GROEN, VRIJ, ROOD, GROEN]
    ]
TIMESTRAIGHT = 2
TIMETURN = 2

GROEN_plekken = []
ROOD_plekken =[]
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == GROEN:
            GROEN_plekken.append((x, y))
for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y] == ROOD:
            ROOD_plekken.append((x, y))
aantalgroen = len(GROEN_plekken)


start = (0, 0)

t1 = time.perf_counter()
snelste_routes = fastestRoute(board, start)
t2 = time.perf_counter()
print(t2-t1)
output_file = lijst_voor_instructiefile(snelste_routes[0])
print('output', output_file)
write_instructionfile(output_file)

#lijst = [(0, 0), (1, 0), (2,0), (3, 0), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (2, 5), (2, 4), (2, 3), (2, 2), (2, 1), (1, 1), (0, 1), (0,0)]
#assert lijst_voor_instructiefile(lijst) == output_file
#print(calculate_time(lijst))