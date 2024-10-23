# Juego simple con Menu y uso de Power-Ups (Poderes)
Este es un simple creado en Python usan la bibliote de pygame. 

# Objetivo
El objetivo del juego es muy simple, consiste en esquivar obstaculos y recoger power-ups que aumentan temporalmente la velocidad del jugador.

# Características
* Menu de inicio: Con opciones de comenzar de iniciar el juego o salir de el.
* Obstaculos: Aparecen en la pantalla y conforme el jugador esquive (avance) ira aumentado la velocidad del juego
* Power-ups Mejora la velocidad del jugador temporalmente , facilitando los obstaculos
* Puntaje: Cada vez que el jugador esquiva un obstaculo, su punta aumenta.

# Requisitos
* Python 3.x
* Biblioteca pygame: Se puede instalar con el siguiente comando; pip install pygame

# ¿Como jugar?
1. Ejecuta el archivo del juego
2. En el menu principal:
   * Presiona "ENTER" para comenzar el juego
   * Presiona "ESC" para salir del juego
3. Usa las teclas de flecha "izquierda" y "derecha" para mover el jugador.
4. Los obstaculos iran callendo desde la parte superior de la pantalla, asi que esquivalos
5. Recoge los power-ups verdes que serviran para aumentar temporalmente la velocidad del jugador
6. Si chocas con algun obstaculo, el juego terminara y se mostrara el puntaje final en la pantalla

# Estructura del codigo
* Show_menu(): Muestra el menu principañ
* game_loop(): Contiene la logica principal del juego, como el movimiento del jugador, los obstaculos, la recoleccion de los poderes y el puntaje
* show_message(): Muestra mensaje en la patanlla, como el puntaje o el estado del juego

# Controles
* Flecha izquierda: Mueve el personaje a la izquierda
* Flecha derecha: Mueve el personaje a la derecha
* Enter: Comienza el juego en el menu
* ESC: Salir del juego


