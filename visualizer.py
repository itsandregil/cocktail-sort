import random

import pygame

# Inicializamos Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Dimensiones de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cocktail Sort Visualizer")

# Configurar la velocidad de visualización
clock = pygame.time.Clock()

def draw_bars(arr, highlight1=None, highlight2=None):
    """Funcion para dibujar las barras en la pantalla."""
    screen.fill(WHITE)
    bar_width = width // len(arr)
    max_val = max(arr)

    for i, val in enumerate(arr):
        color = GREEN if i == highlight1 or i == highlight2 else BLACK
        bar_height = int((val / max_val) * (height - 20))  # Escalar la altura de las barras
        pygame.draw.rect(screen, color, [i * bar_width, height - bar_height, bar_width - 1, bar_height])

    pygame.display.update()

def cocktail_sort(arr: list[int]) -> None:
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Recorrido de izquierda a derecha
        for i in range(start, end):
            draw_bars(arr, i, i+1)
            pygame.time.delay(100)  # Pequeña pausa para visualizar
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Recorrido de derecha a izquierda
        for i in range(end - 1, start - 1, -1):
            draw_bars(arr, i, i+1)
            pygame.time.delay(100)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1

def main():
    running = True
    n_bars = 50  # Número de barras
    random_list = [random.randint(10, 500) for _ in range(n_bars)]  # Lista aleatoria

    cocktail_sort(random_list)  # Ejecutar el algoritmo

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_bars(random_list)

    pygame.quit()

if __name__ == "__main__":
    main()
