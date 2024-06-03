jugador=input("Elige piedra, papel o tijera: ")
computadora="piedra"  # La computadora elige piedra por defecto

print("La computadora elige:", computadora)

# Resultados predefinidos
if jugador == "piedra" and computadora == "tijera":
    print("Ganaste!")
elif jugador == "papel" and computadora == "piedra":
    print("Ganaste!")
elif jugador == "tijera" and computadora == "papel":
    print("Ganaste!")
elif jugador == computadora:
    print("Empate!")
else:
    print("La computadora gana!")
    