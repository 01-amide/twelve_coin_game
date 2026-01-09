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
    screen.blit(text, (x - 12, y - 8))

# ---- CREATE COINS ----
coins = []
labels = [
    "A1","A2","A3","A4",
    "B1","B2","B3","B4",
    "C1","C2","C3","C4"
]

start_x, start_y = 100, 80
x, y = start_x, start_y

for label in labels:
    coins.append({
        "label": label,
        "pos": (x, y)
    })
    x += 80
    if x > 600:
        x = start_x
        y += 80

# ---- MAIN LOOP ----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((240, 240, 240))

    for coin in coins:
        draw_coin(coin["pos"][0], coin["pos"][1], coin["label"])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
