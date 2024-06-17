while True:
    jugador = input("Elige piedra, papel o tijera o salir para terminar: ").lower()
    
    if jugador == "salir":
        print("Gracias por jugar. Hasta la próxima!")
        break  

    if jugador not in ["piedra", "papel", "tijera"]:
        print("Opción no válida. Intenta de nuevo.")
        continue  

    computadora = "piedra"  #En este caso la computadora elige piedra como ejemplo. 
    print("La computadora elige:", computadora)
    
    # Determinar el resultado del juego
    if jugador == computadora:
        print("Empate!")
    elif jugador == "papel":
        print("Ganaste!")
    elif jugador == "tijera":
        print("La computadora gana!")
    elif jugador == "piedra":
        print("Empate!")