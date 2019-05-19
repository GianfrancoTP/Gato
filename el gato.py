tablero = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
terminar = False

print tablero[0],tablero[1],tablero[2]
print tablero[3],tablero[4],tablero[5]
print tablero[6],tablero[7],tablero[8]

intentos = 0
while not terminar or intentos < 9:
    while True:
        print ""
        jugador_1 = raw_input("jugador 1: ")
        if jugador_1 == "1":
            if tablero[0] == "_":
                tablero[0] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "2":
            if tablero[1] == "_":
                tablero[1] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "3":
            if tablero[2] == "_":
                tablero[2] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "4":
            if tablero[3] == "_":
                tablero[3] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "5":
            if tablero[4] == "_":
                tablero[4] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "6":
            if tablero[5] == "_":
                tablero[5] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "7":
            if tablero[6] == "_":
                tablero[6] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "8":
            if tablero[7] == "_":
                tablero[7] = "X"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_1 == "9":
            if tablero[8] == "_":
                tablero[8] = "X"
                break
            else:
                print "ingrese una opcion valida"
        else:
            print "ingrese una opcion valida"

    print tablero[0],tablero[1],tablero[2]
    print tablero[3],tablero[4],tablero[5]
    print tablero[6],tablero[7],tablero[8]

    if tablero[0]+tablero[1]+tablero[2] == "XXX" or tablero[3]+tablero[4]+tablero[5] == "XXX" or tablero[6]+tablero[7]+tablero[8] == "XXX" \
            or tablero[0]+tablero[3]+tablero[6] == "XXX" or tablero[1]+tablero[4]+tablero[7] == "XXX" or tablero[2]+tablero[5]+tablero[8] == "XXX" \
            or tablero[0]+tablero[4]+tablero[8] == "XXX" or tablero[6]+tablero[4]+tablero[2] == "XXX":
        print ""
        print "Jgador UNO ha ganado!!"
        break
    intentos += 1
    if intentos >= 9:
        break
    while True:
        print ""
        jugador_2 = raw_input("jugador 2: ")
        if jugador_2 == "1":
            if tablero[0] == "_":
                tablero[0] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "2":
            if tablero[1] == "_":
                tablero[1] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "3":
            if tablero[2] == "_":
                tablero[2] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "4":
            if tablero[3] == "_":
                tablero[3] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "5":
            if tablero[4] == "_":
                tablero[4] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "6":
            if tablero[5] == "_":
                tablero[5] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "7":
            if tablero[6] == "_":
                tablero[6] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "8":
            if tablero[7] == "_":
                tablero[7] = "O"
                break
            else:
                print "ingrese una opcion valida"
        elif jugador_2 == "9":
            if tablero[8] == "_":
                tablero[8] = "O"
                break
            else:
                print "ingrese una opcion valida"
        else:
            print "ingrese una opcion valida"
    print tablero[0], tablero[1], tablero[2]
    print tablero[3], tablero[4], tablero[5]
    print tablero[6], tablero[7], tablero[8]

    if tablero[0]+tablero[1]+tablero[2] == "OOO" or tablero[3]+tablero[4]+tablero[5] == "OOO" or tablero[6]+tablero[7]+tablero[8] == "OOO" \
            or tablero[0]+tablero[3]+tablero[6] == "OOO" or tablero[1]+tablero[4]+tablero[7] == "OOO" or tablero[2]+tablero[5]+tablero[8] == "OOO" \
            or tablero[0]+tablero[4]+tablero[8] == "OOO" or tablero[6]+tablero[4]+tablero[2] == "OOO":
        print ""
        print "Jgador DOS ha ganado!!"
        break
    intentos += 1
print "juego Terminado"