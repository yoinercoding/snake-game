import pygame
import random

# Inicializar Pygame
pygame.init()

# Establecer el tamaño de la pantalla
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# Establecer el título de la ventana
pygame.display.set_caption("Snake Game")

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Definir la velocidad de la serpiente
speed = 10

# Definir el tamaño de la serpiente y la comida
size = 10

# Definir la posición inicial de la serpiente
x = width / 2
y = height / 2

# Definir la dirección inicial de la serpiente
direction = "right"

# Definir la posición inicial de la comida
food_x = round(random.randrange(0, width - size) / 10.0) * 10.0
food_y = round(random.randrange(0, height - size) / 10.0) * 10.0

# Definir la longitud inicial de la serpiente
length = 1
snake_list = []

# Función para dibujar la serpiente
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], size, size])

# Loop principal del juego
game_over = False
clock = pygame.time.Clock()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Cambiar la dirección de la serpiente con las flechas del teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    # Mover la serpiente
    if direction == "right":
        x += speed
    elif direction == "left":
        x -= speed
    elif direction == "up":
        y -= speed
    elif direction == "down":
        y += speed

    # Si la serpiente sale de la pantalla, el juego termina
    if x >= width or x < 0 or y >= height or y < 0:
        game_over = True

    # Si la serpiente come la comida, se incrementa la longitud
    if x == food_x and y == food_y:
        food_x = round(random.randrange(0, width - size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - size) / 10.0) * 10.0
        length += 1

    # Dibujar la pantalla y los objetos
    screen.fill(black)
    pygame.draw.rect(screen, red, [food_x, food_y, size, size])

    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    draw_snake(snake_list)
    pygame.display.update()

    # Establecer la velocidad del juego
    clock.tick(25)

# quit
pygame.quit()
