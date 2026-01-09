import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12 Coin Puzzle")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

def draw_coin(x, y, label):
    pygame.draw.circle(screen, (200, 200, 0), (x, y), 20)
    text = font.render(label, True, (0, 0, 0))
    screen.blit(text, (x - 10, y - 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))
    draw_coin(100, 100, "A1")
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
