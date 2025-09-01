print("******** Pidra Papel Tijeras ********"
      "\nEscoge Piedra=p, Papel=pa,Tijeras=t ")

juego=True
jugador1= input("Juego jugador 1 : \n")
jugador2= input("Juego jugador 2 : \n")
diccionario={"p":"piedra","pa":"papel","t":"tijeras"}

if jugador1 in diccionario:
    print("Juego Jugador 1: ",diccionario[jugador1])
else:
    print("Jugada no encontrada para el jugado 1")
    juego=False

if jugador2 in diccionario:
    print("Juego Jugador 2: ",diccionario[jugador2])
else:
    print("Jugada no encontrada para el jugado 2")
    juego=False

if juego == True:
    
    if jugador1==jugador2:
        print("Empate")
    elif jugador1=="p" and jugador2=="t" :
        print("Gana Jugador 1")
    elif jugador1=="t" and jugador2=="p":
        print("Gana Jugador 2")
    elif jugador1=="pa" and jugador2=="t" :
        print("Gana Jugador 2")
    elif jugador1=="t" and jugador2=="pa":
        print("Gana Jugador 1")
    elif jugador1=="pa" and jugador2=="p" :
        print("Gana Jugador 1")
    elif jugador1=="p" and jugador2=="pa":
         print("Gana Jugador 2")    
else:
    print("Juego Finalizado por inconsistencia de datos")        


