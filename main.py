import pygame
import sys
import math
import random

# ------------------ INIT ------------------
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("12 Coin Puzzle")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

COIN_RADIUS = 20

LEFT_PAN_POS = (250, 420)
RIGHT_PAN_POS = (550, 420)

# ------------------ COUNTERFEIT SETUP ------------------
ALL_COINS = [
    "A1","A2","A3","A4",
    "B1","B2","B3","B4",
    "C1","C2","C3","C4"
]

fake_coin = random.choice(ALL_COINS)
fake_type = random.choice(["heavier", "lighter"])

# (For debugging ONLY — you can comment this out later)
print("FAKE:", fake_coin, fake_type)

def get_weight(label):
    if label == fake_coin:
        return 11 if fake_type == "heavier" else 9
    return 10

# ------------------ DRAW HELPERS ------------------
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

def draw_pan(center_x, center_y, label):
    pygame.draw.rect(
        screen,
        (180, 180, 180),
        (center_x - 120, center_y - 30, 240, 60),
        border_radius=10
    )
    text = font.render(label, True, (0, 0, 0))
    screen.blit(text, (center_x - 40, center_y - 50))

# ------------------ CREATE COINS ------------------
coins = []
labels = ALL_COINS

start_x, start_y = 100, 80
x, y = start_x, start_y

for label in labels:
    coins.append({
        "label": label,
        "pos": (x, y),
        "selected": False,
        "zone": "pool"
    })
    x += 80
    if x > 600:
        x = start_x
        y += 80

# ------------------ GAME STATE ------------------
weigh_result = ""

# ------------------ MAIN LOOP ------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ---- MOUSE CLICK (SELECT COINS) ----
        if event.type == pygame.MOUSEBUTTONDOWN:
            for coin in coins:
                if coin_clicked(coin["pos"], event.pos):
                    coin["selected"] = not coin["selected"]

        # ---- KEYBOARD INPUT ----
        if event.type == pygame.KEYDOWN:

            # Move to LEFT pan
            if event.key == pygame.K_l:
                for coin in coins:
                    if coin["selected"]:
                        coin["zone"] = "left"
                        coin["selected"] = False

            # Move to RIGHT pan
            if event.key == pygame.K_r:
                for coin in coins:
                    if coin["selected"]:
                        coin["zone"] = "right"
                        coin["selected"] = False

            # Return to POOL
            if event.key == pygame.K_p:
                for coin in coins:
                    if coin["selected"]:
                        coin["zone"] = "pool"
                        coin["selected"] = False

            # ---- WEIGH ----
            if event.key == pygame.K_w:
                left_weight = 0
                right_weight = 0

                for coin in coins:
                    if coin["zone"] == "left":
                        left_weight += get_weight(coin["label"])
                    elif coin["zone"] == "right":
                        right_weight += get_weight(coin["label"])

                if left_weight == right_weight:
                    weigh_result = "BALANCE"
                elif left_weight > right_weight:
                    weigh_result = "LEFT_HEAVY"
                else:
                    weigh_result = "RIGHT_HEAVY"

    # ------------------ DRAW ------------------
    screen.fill((240, 240, 240))

    draw_pan(*LEFT_PAN_POS, "LEFT PAN")
    draw_pan(*RIGHT_PAN_POS, "RIGHT PAN")

    pool_x, pool_y = 100, 80
    left_x, left_y = LEFT_PAN_POS[0] - 90, LEFT_PAN_POS[1]
    right_x, right_y = RIGHT_PAN_POS[0] - 90, RIGHT_PAN_POS[1]

    for coin in coins:
        if coin["zone"] == "pool":
            coin["pos"] = (pool_x, pool_y)
            pool_x += 80
            if pool_x > 600:
                pool_x = 100
                pool_y += 80

        elif coin["zone"] == "left":
            coin["pos"] = (left_x, left_y)
            left_x += 60

        elif coin["zone"] == "right":
            coin["pos"] = (right_x, right_y)
            right_x += 60

        draw_coin(
            coin["pos"][0],
            coin["pos"][1],
            coin["label"],
            coin["selected"]
        )

    # ---- DISPLAY RESULT ----
    if weigh_result:
        text = font.render(f"Result: {weigh_result}", True, (0, 0, 0))
        screen.blit(text, (300, 520))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
