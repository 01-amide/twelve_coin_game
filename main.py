import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12 Coin Puzzle")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

COIN_RADIUS = 20

def draw_coin(x, y, label, selected):
    pygame.draw.circle(screen, (200, 200, 0), (x, y), COIN_RADIUS)
    border_color = (255, 0, 0) if selected else (0, 0, 0)
    pygame.draw.circle(screen, border_color, (x, y), COIN_RADIUS, 2)
    text = font.render(label, True, (0, 0, 0))
    screen.blit(text, (x - 12, y - 8))

def coin_clicked(coin_pos, mouse_pos):
    dx = coin_pos[0] - mouse_pos[0]
    dy = coin_pos[1] - mouse_pos[1]
    return math.hypot(dx, dy) <= COIN_RADIUS

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
        "pos": (x, y),
        "selected": False
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

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for coin in coins:
                if coin_clicked(coin["pos"], mouse_pos):
                    coin["selected"] = not coin["selected"]

    screen.fill((240, 240, 240))

    for coin in coins:
        draw_coin(
            coin["pos"][0],
            coin["pos"][1],
            coin["label"],
            coin["selected"]
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
