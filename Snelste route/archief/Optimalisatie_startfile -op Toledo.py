
TIMESTRAIGHT = 3    # tijd nodig om één vakje vooruit te rijden
TIMETURN = 4       # tijd nodig om binnen één vakje een kwart slag te draaien

ACCEPT = 'accept'
ABANDON = 'abandon'
CONTINUE = 'continue'


# INITIALISATIE

def initiate_board(nbRows,nbCols):
    """
    De functie maakt een nieuw leeg bord aan met nbRows rijen en nbCols kolommen.

    Het bord is een matrix bestaande uit nbRows rijen en nbCols kolommen. Elk vakje bevat telkens een spatie
    (" ") om aan te duiden dat het vakje leeg is.

    Deze functie geeft het bord terug.
    Wanneer er een ongeldige invoer is (nbRows is < 1, nbCols is < 1),
    wordt 'None' teruggegeven.
    """


    return None

def putGreen(board,x,y):
    """
        De functie plaatst een groen schijfje , een "G", op het bord op rijcoördinaat x en kolomcoördinaat y.

        De functie geeft het bord terug, met op de gegeven coördinaten de letter "G" om aan te geven dat hier
        een groen schijfje ligt.

        Indien x of y niet overeenkomt met de dimensies van het bord, zal het bord ongewijzigd gelaten worden.
    """


    return None


def putRed(board, x, y):
    """
        De functie plaatst een rood schijfje op het bord op rijcoördinaat x en kolomcoördinaat y.

        De functie geeft het bord terug, met op de gegeven coördinaten de letter "R" om aan te geven dat hier
        een rood schijfje ligt.

        Indien x of y niet overeenkomt met de dimensies van het bord, zal het bord ongewijzigd gelaten worden.
    """


    return None


###################################################################################################################
############# HULP-FUNCTIES ######################################################################################
###################################################################################################################

def getGreens(board):
    """
        De functie geeft een set terug met de posities van alle groene schijfjes van het bord
    """

    return None

def getReds(board):
    """
        De functie geeft een set terug met de posities van alle rode schijfjes van het bord
    """

    return None

def getLegalNeighbours(board,pos):
    """
        De functie geeft een set terug met alle toegestane posities waar een wagentje naar toe kan
        bewegen vanuit de gegeven positie 'pos'. De functie houdt daarbij rekening met de randen van het bord en
        de posities waar er zich een rood schijfje bevindt.
    """

    return None

def calculateTime(route):
    """
        De functie berekent de tijd die het wagentje nodig heeft om de gegeven route te rijden. De functie gebruikt
        hiervoor de constanten TIMESTRAIGHT en TIMETURN.

        Je mag ervan uitgaan dat het wagentje op de startpositie van de route de juiste oriëntatie bevat en niet meer
        hoeft te draaien om de eerste stap te zetten.

        Je mag ervan uitgaan dat route een geldige route is, zijnde een lijst van tupels die de achtereenvolgende coördinaten
        bevat waar het wagentje zich stap voor stap bevindt.
    """

    return None


def makeInstructionfile(route, board):
    """
        De functie genereert een .txt-bestand dat kan gebruikt worden je wagentje de opgegeven route te laten rijden op het
        opgegeven board.

        Elke regel van het bestand drie met een komma van elkaar gescheiden waarden, namelijk:
        rijnummer, kolomnummer, True/False
        waarbij de derde waarde een boolean is die aangeeft of er op de gegeven positie een groen schijfje dient opgepikt
        te worden.

        De functie gaat ervan uit dat "route" een geldige route is voor het opgegeven "board".
    """
    file = open('../instructions.txt', 'w')
    for pos in route:
        pick = "False"
        if board[pos[0]][pos[1]] == "G":
            pick = "True"
        outputstring = str(pos[0])+", "+str(pos[1]) +", " + pick + "\n"
        file.write(outputstring)
    file.close()


###################################################################################################################
############# BACKTRACKING - sub-optimaal #########################################################################
###################################################################################################################

# In deze variant mag je gebruik maken van de functie 'fastestRoute' die alvast de snelste
# route tussen twee willekeurige posities op het bord bepaalt.
# Gebruik makend van deze functie kan je zelf de snelste route bepalen waarmee alle groene schijfjes
# kunnen opgepikt worden door deze route te interpreteren als een aaneenschakeling van snelste routes tussen twee
# groene schijfjes onderling.
# Let wel, dit algoritme geeft niet altijd de juiste oplossing voor de 'totale' snelste route, omdat het geen rekening
# houdt met de eventuele draaitijden op de vakjes waar groene schijfjes liggen.

def examine_help():
    """
        examine-functie voor de 'fastestRoute'-backtracking.
    """
    return None

def extend_help():
    """
        extend-functie voor de 'fastestRoute'-backtracking.
    """
    return None

def solve_help():
    """
        solve-functie voor de 'fastestRoute'-backtracking.
    """
    return None

def fastestRoute(board, start, finish):
    """
        De functie geeft de snelste route terug  om van de positie 'start' naar de positie 'finish' te rijden op
        het gegeven bord. De route vermijdt daarbij de posities waar rode schijfjes aanwezig zijn.

        Je mag ervan uitgaan dat start en finish beiden tupels zijn met een x- en een y-coördinaat die de dimensies
        van het gegeven bord respecteren.

        Dit zal Prof. Holvoet samen met jullie bekijken in de les in semesterweek 9.
    """

    return None



def examine():
    """
        examine-functie voor de 'collect'-backtracking.
    """
    return None

def extend():
    """
        extend-functie voor de 'collect'-backtracking.
    """
    return None

def solve():
    """
        solve-functie voor de 'collect'-backtracking.
    """
    return None


def collect(board,start,finish):
    """
        Deze functie geeft de snelste route terug om van de positie 'start' naar de positie 'finish' te rijden op
        het gegeven bord, waarbij de posities van alle groene schijfjes onderweg worden aangedaan door de route.

        Deze functie maakt gebruik van de hulpfunctie 'fastestRoute' en berekent de snelste route als een
        aaneenschakeling van snelste routes tussen twee groene schijfjes onderling.

        De functie houdt geen rekening met eventuele draaitijden die het wagentje nodig heeft om op de plek van het
        groene schijfje zelf eventueel van richting te veranderen.
    """
    return None


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


