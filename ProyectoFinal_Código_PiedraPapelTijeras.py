import random  # Primero debemos importar el módulo random.

# Definimos las variables de partidas ganadas y perdidas. 
ganadas=0
perdidas=0

# Se genera esta variable para que el juego pueda ser jugado reiteradas veces.
continuar_juego=True

# Comienza el juego
while continuar_juego:
    # Se solicita al jugador una opción
    jugador=input("Elige piedra, papel o tijera o 'salir' para terminar: ").lower()
    
    # Se ejecuta cuando el jugador desee salir del juego. 
    if jugador=="salir":
        print("Gracias por jugar. Hasta la próxima!")
        break  # Se sale del bucle y se da el juego cómo terminado.

    # Se verifica que la entrada del jugador sea válida. 
    if jugador not in ("piedra", "papel", "tijera"):
        print("Opción no válida. Intenta de nuevo.")
        continue  # Se regresa al inicio del bucle y se pide otra entrada que sea válida. 

    # La computadora elige aleatoriamente entre piedra, papel o tijera.
    opciones=("piedra", "papel", "tijera")
    computadora=random.choice(opciones)
    print("La computadora elige:", computadora)
    
    # Determinar el resultado del juego.
    if jugador == computadora:
        print("Se ha determiando un empate!")
    elif jugador == "piedra" and computadora == "tijera":
        print("Se determinó que ganaste esta partida!")
        ganadas += 1  # Incrementa el contador de partidas ganadas.
    elif jugador == "papel" and computadora == "piedra":
        print("Se determinó que ganaste esta partida!")
        ganadas += 1  # Incrementa el contador de partidas ganadas.
    elif jugador == "tijera" and computadora == "papel":
        print("Se determinó que ganaste esta partida!")
        ganadas += 1  # Incrementa el contador de partidas ganadas.
    else:
        print("Se ha dado a la computadora como ganadora!")
        perdidas += 1  # Incrementa el contador de partidas perdidas.

    # Mostrar el conteo de partidas ganadas y perdidas.
    print("Llevas: ", ganadas, "partidas ganadas")
    print("Llevas: ", perdidas, "partidas perdidas")

# Mensaje final con el total de partidas ganadas y perdidas.
print("Total de partidas ganadas: ", ganadas)
print("Total de partidas perdidas: ", perdidas)