import pygame
from time import sleep
from pygame.locals import *
from entities.player import Player
from entities.shot import Shot

pygame.init()
screen = pygame.display.set_mode((500, 500))
p1 = Player("p1", (43, 65, 194), (450, 50))
p2 = Player("p2", (128, 25, 41), (50, 450))

p1_shoot_interval = True
p2_shoot_interval = True

players = [p1, p2]

p1_shots = []
p2_shots = []

players_speed = 4

hp_font = pygame.font.SysFont("Courier New", 24)

def render_objects():
    screen.fill((255, 255, 255))

    p1_hp_display = hp_font.render(f"Cyan's HP: {p1.hp}", True, (93, 133, 245))
    p2_hp_display = hp_font.render(f"Oranges's HP: {p2.hp}", True, (222, 119, 51))

    screen.blit(p1_hp_display, (300, 10))
    screen.blit(p2_hp_display, (10, 10))

    for player in players:
        pygame.draw.circle(screen, player.color, player.coords, 40)

    for shot in p1.shots:

        # -- 
        if p2.findShot(shot) != -1:
            p1.shots.remove(shot)
            p2.shot.remove(shot)

        if (p2.hit(shot.coords)):
            p2.hp -= 10
            p1.shots.remove(shot)
        
        if (shot.coords[0] < 0):
            p1.shots.remove(shot)
        else:
            pygame.draw.circle(screen, shot.color, shot.coords, shot.radius)
            shot.coords = (shot.coords[0] - shot.speed, shot.coords[1])

    for shot in p2.shots:
        if (p1.hit(shot.coords)):
            p1.hp -= 10
            p2.shots.remove(shot)
        if (shot.coords[0] > 500):
            p2.shots.remove(shot)
        else:
            pygame.draw.circle(screen, shot.color, shot.coords, shot.radius)
            shot.coords = (shot.coords[0] + shot.speed, shot.coords[1])
            
status = True
while status:
    render_objects()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            status = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if (p1_shoot_interval):
                    p1.shoot((60, 107, 201), 2)
                p1_shoot_interval = not p1_shoot_interval

            if event.key == pygame.K_d:
                if (p2_shoot_interval):
                    p2.shoot((199, 52, 42), 2)
            p2_shoot_interval = not p2_shoot_interval

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and p1.coords[1] > 20:
        p1.moveUp(players_speed)
    if keys[pygame.K_DOWN] and p1.coords[1] < 480:
        p1.moveDown(players_speed)
    if keys[pygame.K_w] and p2.coords[1] > 20:
        p2.moveUp(players_speed)
    if keys[pygame.K_s] and p2.coords[1] < 480:
        p2.moveDown(players_speed) 

    pygame.display.update()
    sleep(0.01)

pygame.quit()
exit()

# FIX HITBOX -- check
# SLOW DOW SHOTS -- check
# MAKE KEY PRESS -- check
# ABSTRACT
# MAKE BULLET COLLISION 