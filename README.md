Repositorio correspondiente al juego de piedra, papel o tijera. Dónde el usuario se enfrenta a la computadora pudiendo jugar reiteradas veces contra la misma hasta que él lo desee, se añaden contadores para saber las partidas ganadas y perdidas, cómo también se hace uso de la biblioteca random en Python para generar una respuesta aleatoria de parte de la computadora. Se adjunta un archivo ".rar" con un documento de texto con las instrucciones para poder ejecutar la interfaz gráfica desarrollada para el juego, mediante la librería "Pygame".

Funcionalidades del Juego: 

Importación del módulo random: Se importa el módulo random para generar elecciones aleatorias para la computadora.

Variables de la partida: Ganadas y perdidas se utilizan para llevar el conteo de las partidas ganadas y perdidas por el jugador.

Bucle del juego: Un bucle while permite que el juego continúe hasta que el jugador decida salir.

Entrada del jugador: Se solicita al jugador que elija entre "piedra", "papel", "tijera" o "salir" para terminar el juego. Si el jugador elige "salir" el juego finaliza. 

Validación de la entrada: Si la entrada no es válida, se muestra un mensaje de error y se pide una nueva entrada.

Elección aleatoria de la computadora: La computadora elige aleatoriamente entre "piedra", "papel" o "tijera" utilizando random.choice.

Determinación del resultado: Se compara la elección del jugador con la de la computadora para determinar el resultado (ganar, perder o empate).

Mostrar resultados: Después de cada ronda, se muestran las partidas ganadas y perdidas hasta el momento.

Mensaje final: Cuando el jugador decide salir, se muestra un mensaje final con el total de partidas ganadas y perdidas.

Gracias por jugar y disfrutar del proyecto de Piedra, Papel o Tijera!

