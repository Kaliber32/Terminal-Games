import random

size = 10
play = True

print()
print("Willkommen zu Schiffe Versenken!")
print()
print("Das sind die verschiedenen Schiffe:")
print()
print("1x Schlachtschiff (5 Felder)")
print("1x Kreuzer (4 Felder)")
print("2x Zerstörer (3 Felder)")
print("2x U-Boote (2 Felder)")
print()

spieler1 = [
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'b', 'b', 'b', 'b', 'b', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
]

spieler2 = [
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'b', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'b', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'b', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'b', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
    ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']
]

max_treffer = 0

for i in range(size):
    for j in range(size):
        if spieler2[i][j] == 'b':
            max_treffer += 1

spieler1_board = [[None for _ in range(10)] for _ in range(10)]
spieler2_board = [[None for _ in range(10)] for _ in range(10)]

while play:
    g_treffer_1 = 0
    g_treffer_2 = 0
    print("Spieler 1 ist dran.")
    print()
    feld = input("Dein Feld: ")

    for i in range(size):
        for j in range(size):
            z = 0
            zahl2 = False
            zahl22 = False
            number12 = 100
            number22 = 100
            for number in feld:
                z = z + 1
                if number != "," and (z == 1 or z == 2):
                    if z == 1:
                        number11 = number
                    else:
                        number12 = number
                if zahl2 == True:
                    if zahl22 == False:
                        zahl22 = True
                        number21 = number
                    else:
                        number22 = number
                if number == ",":
                    zahl2 = True
            if number12 != 100:
                z = int(number11 + number12)
            else:
                z = int(number11)
            if number22 != 100:
                k = int(number21 + number22)
            else:
                k = int(number21)

    if spieler2[z-1][k-1] == 'b':
        spieler1_board[z-1][k-1] = 'X'
    else:
        spieler1_board[z-1][k-1] = 'O'

    for i in range(size):
        print("_"*(6*size+1))
        for j in range(size):
            if spieler1_board[i][j] == 'O':
                print("|  O  ", end="")
            elif spieler1_board[i][j] == 'X':
                g_treffer_1 += 1
                print("|  X  ", end="")
            else:
                print("|     ", end="")
        print("|")

    print("_"*(6*size+1))
    
    if g_treffer_1 == max_treffer:
        print()
        print(f"Spieler Nr. 1 hat gewonnen und {max_treffer} Treffer gelandet!") 
        exit()

    print()
    print("Spieler 2 ist dran.")
    print()

    feld = input("Dein Feld: ")

    for i in range(size):
        for j in range(size):
            z = 0
            zahl2 = False
            zahl22 = False
            number12 = 100
            number22 = 100
            for number in feld:
                z = z + 1
                if number != "," and (z == 1 or z == 2):
                    if z == 1:
                        number11 = number
                    else:
                        number12 = number
                if zahl2 == True:
                    if zahl22 == False:
                        zahl22 = True
                        number21 = number
                    else:
                        number22 = number
                if number == ",":
                    zahl2 = True
            if number12 != 100:
                z = int(number11 + number12)
            else:
                z = int(number11)
            if number22 != 100:
                k = int(number21 + number22)
            else:
                k = int(number21)

    if spieler1[z-1][k-1] == 'b':
        spieler2_board[z-1][k-1] = 'X'
    else:
        spieler2_board[z-1][k-1] = 'O'

    for i in range(size):
        print("_"*(6*size+1))
        for j in range(size):
            if spieler2_board[i][j] == 'O':
                print("|  O  ", end="")
            elif spieler2_board[i][j] == 'X':
                print("|  X  ", end="")
                g_treffer_2 += 1
            else:
                print("|     ", end="")
        print("|")

    print("_"*(6*size+1))
    print()
    if g_treffer_2 == max_treffer:
        print(f"Spieler Nr. 2 hat gewonnen und {max_treffer} Treffer gelandet!") 
        play = False