import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Piedra, Papel o Tijera")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
light_gray = (200, 200, 200)

# Fuentes
font = pygame.font.Font(None, 36)
medium_font = pygame.font.Font(None, 48)
large_font = pygame.font.Font(None, 72)

# Cargar imágenes
rock_img = pygame.image.load('piedra.png')
paper_img = pygame.image.load('papel.png')
scissors_img = pygame.image.load('tijera.png')

# Redimensionar imágenes
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Posiciones de los botones
rock_rect = rock_img.get_rect(center=(200, 500))
paper_rect = paper_img.get_rect(center=(400, 500))
scissors_rect = scissors_img.get_rect(center=(600, 500))

# Variables de juego
ganadas = 0
perdidas = 0
jugador = ""
computadora = ""
resultado = ""

# Botón de salida
exit_button = pygame.Rect(700, 20, 80, 40)

# Función para dibujar el botón
def draw_button(rect, color, text):
    pygame.draw.rect(win, color, rect)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect(center=rect.center)
    win.blit(text_surface, text_rect)

# Función principal del juego
def main():
    global jugador, computadora, resultado, ganadas, perdidas
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if rock_rect.collidepoint(mouse_pos):
                    jugador = "piedra"
                elif paper_rect.collidepoint(mouse_pos):
                    jugador = "papel"
                elif scissors_rect.collidepoint(mouse_pos):
                    jugador = "tijera"
                elif exit_button.collidepoint(mouse_pos):
                    run = False
                else:
                    continue
                
                opciones = ("piedra", "papel", "tijera")
                computadora = random.choice(opciones)
                
                if jugador == computadora:
                    resultado = "Empate!"
                elif (jugador == "piedra" and computadora == "tijera") or \
                     (jugador == "papel" and computadora == "piedra") or \
                     (jugador == "tijera" and computadora == "papel"):
                    resultado = "Ganaste!"
                    ganadas += 1
                else:
                    resultado = "Perdiste!"
                    perdidas += 1
        
        # Dibujar elementos en la ventana
        win.fill(white)
        pygame.draw.rect(win, light_gray, (0, 450, width, 150))  # Área de selección

        # Títulos
        title_text = large_font.render("Piedra, Papel o Tijera", True, black)
        win.blit(title_text, (width // 2 - title_text.get_width() // 2, 20))

        # Instrucciones
        instructions_text = font.render("Elige tu opción:", True, black)
        win.blit(instructions_text, (width // 2 - instructions_text.get_width() // 2, 380))

        # Imágenes de opciones
        win.blit(rock_img, rock_rect)
        win.blit(paper_img, paper_rect)
        win.blit(scissors_img, scissors_rect)
        
        # Mostrar elección de la computadora
        computadora_text = medium_font.render(f"Computadora: {computadora}", True, blue)
        win.blit(computadora_text, (width // 2 - computadora_text.get_width() // 2, 200))
        
        # Mostrar resultado
        resultado_text = medium_font.render(resultado, True, green if resultado == "Ganaste!" else red)
        win.blit(resultado_text, (width // 2 - resultado_text.get_width() // 2, 260))
        
        # Mostrar conteo de partidas ganadas y perdidas
        ganadas_text = font.render(f"Ganadas: {ganadas}", True, black)
        win.blit(ganadas_text, (50, 120))
        perdidas_text = font.render(f"Perdidas: {perdidas}", True, black)
        win.blit(perdidas_text, (50, 160))
        
        # Dibujar botón de salida
        draw_button(exit_button, yellow, "Salir")
        
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()
