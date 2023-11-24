import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])

winner = {
    "name": "",
    "color": (43, 65, 194)
}

screen.fill((18, 18, 23))

font_title = pygame.font.SysFont("Courier New", 42)
title = font_title.render("Game Over", True, (204, 31, 77))

font_subtitle = pygame.font.SysFont("Courier New", 24)
subtitle = font_subtitle.render(f"{winner['name']} Player won!", True, winner["color"])


status = True
while status:
    screen.blit(title, (140, 180))
    screen.blit(subtitle, (140, 230))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    pygame.display.update()


pygame.quit()