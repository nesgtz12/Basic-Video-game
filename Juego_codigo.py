import pygame
import random

# Inicialización de pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego simple con Menú y Power-Ups')

# Velocidad del juego
clock = pygame.time.Clock()

# Definir el personaje
player_width = 50
player_height = 50
player_speed = 5

# Definir el obstáculo
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

# Definir el power-up
powerup_width = 30
powerup_height = 30
powerup_speed = 2
powerup_active = False
powerup_duration = 3000  # Duración en milisegundos

# Fuente para el texto
font = pygame.font.SysFont(None, 55)

# Función para mostrar texto en pantalla
def show_message(text, color, x, y):
    message = font.render(text, True, color)
    screen.blit(message, [x, y])

# Función para mostrar el menú
def show_menu():
    while True:
        screen.fill(WHITE)
        show_message('Juego Simple', BLACK, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
        show_message('Presiona ENTER para Iniciar', BLACK, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        show_message('Presiona ESC para Salir', BLACK, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 + 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Iniciar el juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

# Función principal del juego
def game_loop():
    global player_speed
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height - 10
    obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    score = 0
    obstacle_speed = 5
    powerup_x = random.randint(0, SCREEN_WIDTH - powerup_width)
    powerup_y = -powerup_height
    powerup_timer = 0

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed

        # Mover el obstáculo
        obstacle_y += obstacle_speed

        # Si el obstáculo sale de la pantalla, reaparece arriba
        if obstacle_y > SCREEN_HEIGHT:
            obstacle_y = -obstacle_height
            obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            score += 1
            obstacle_speed += 0.5  # Incrementar la velocidad con el tiempo

        # Mover el power-up
        if not powerup_active:
            powerup_y += powerup_speed
            if powerup_y > SCREEN_HEIGHT:
                powerup_y = -powerup_height
                powerup_x = random.randint(0, SCREEN_WIDTH - powerup_width)

        # Detectar colisiones con el obstáculo
        if (player_x < obstacle_x + obstacle_width and
            player_x + player_width > obstacle_x and
            player_y < obstacle_y + obstacle_height and
            player_y + player_height > obstacle_y):
            game_over = True

        # Detectar colisiones con el power-up
        if (not powerup_active and
            player_x < powerup_x + powerup_width and
            player_x + player_width > powerup_x and
            player_y < powerup_y + powerup_height and
            player_y + player_height > powerup_y):
            powerup_active = True
            powerup_y = SCREEN_HEIGHT  # Mover el power-up fuera de la vista
            player_speed += 2  # Aumentar la velocidad del jugador
            powerup_timer = pygame.time.get_ticks()  # Reiniciar el temporizador

        # Verificar si el power-up ha expirado
        if powerup_active and pygame.time.get_ticks() - powerup_timer > powerup_duration:
            powerup_active = False
            player_speed -= 2  # Restablecer la velocidad del jugador

        # Dibujar en la pantalla
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [player_x, player_y, player_width, player_height])
        pygame.draw.rect(screen, RED, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
        
        # Dibujar el power-up
        if not powerup_active:
            pygame.draw.rect(screen, GREEN, [powerup_x, powerup_y, powerup_width, powerup_height])

        # Mostrar el puntaje
        show_message(f'Puntaje: {score}', BLACK, 10, 10)

        if game_over:
            show_message('¡Juego terminado!', RED, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
            pygame.display.update()
            pygame.time.delay(2000)
            running = False

        pygame.display.update()
        clock.tick(60)  # Controlar la velocidad del juego

# Ejecutar el menú y luego el juego
show_menu()
game_loop()

# Cerrar Pygame
pygame.quit()
