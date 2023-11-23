from time import sleep
import pygame

from entities.player import Player


class testGame:
  status = True
  fps = pygame.time.Clock()

  objects = []

  font_HUD_player = pygame.font.SysFont("Arial", 50)
  font_HUD_points = pygame.font.SysFont("Arial", 30)
  font_show_info = pygame.font.SysFont("Arial", 10)

  circle = {"x": 50, "y": 50, "direction": "right", "radius": 20}

  p1 = Player("p1", (43, 65, 194), (450, 50))
  p2 = Player("p2", (128, 25, 41), (50, 450))

  p1_shoot_interval = True
  p2_shoot_interval = True

  players = [p1, p2]

  p1_shots = []
  p2_shots = []

  font = pygame.font.SysFont("Courier New", 24)

  def __init__(self):
    pass

  def render_objects(self, screen):
    screen.fill((255, 255, 255))

    p1_hp_display = font.render(f"Cyan's HP: {p1.hp}", True, (93, 133, 245))
    p2_hp_display = font.render(f"Oranges's HP: {p2.hp}", True, (222, 119, 51))

    screen.blit(p1_hp_display, (300, 10))
    screen.blit(p2_hp_display, (10, 10))

    for player in players:
      pygame.draw.circle(screen, player.color, player.coords, 40)

    for shot in p1.shots:
      if (p2.isInHitBox(shot.coords)):
        p2.hp -= 10
        p1.shots.remove(shot)
      
      if (shot.coords[0] < 0):
        p1.shots.remove(shot)
      else:
        pygame.draw.circle(screen, shot.color, shot.coords, shot.radius)
        shot.coords = (shot.coords[0] - shot.speed, shot.coords[1])

    for shot in p2.shots:
      if (p1.isInHitBox(shot.coords)):
        p1.hp -= 10
        p2.shots.remove(shot)
      if (shot.coords[0] > 500):
        p2.shots.remove(shot)
      else:
        pygame.draw.circle(screen, shot.color, shot.coords, shot.radius)
        shot.coords = (shot.coords[0] + shot.speed, shot.coords[1])
          
  def start(self):
    while status:
      self.render_objects()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          status = False
        
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            if (p1.coords[1] > 20):
              p1.moveUp(20)

          if event.key == pygame.K_DOWN:
            if (p1.coords[1] < 480):
              p1.moveDown(20)

          if event.key == pygame.K_LEFT:
            if (p1_shoot_interval):
              p1.shoot((60, 107, 201))
            p1_shoot_interval = not p1_shoot_interval

          if event.key == pygame.K_w:
            if (p2.coords[1] > 20):
              p2.moveUp(20)

          if event.key == pygame.K_s:
            if (p2.coords[1] < 480):
              p2.moveDown(20)

          if event.key == pygame.K_d:
            if (p2_shoot_interval):
              p2.shoot((199, 52, 42))
            p2_shoot_interval = not p2_shoot_interval

    pygame.display.update()
    sleep(0.1)
  # ---HUD---
  # screen.blit(font_show_info.render('FPS: %.1f' % fps.get_fps(), 1, (100, 0, 50)), (10, 10))
  # screen.blit(font_show_info.render('Time: ' + str(fps.get_time()), 1, (100, 0, 50)), (10, 20))
  
  # pygame.display.update()
  # fps.tick(120)
  
  # if(circle["direction"] == "right" and circle["x"] < circle["radius"]):
  #   print("right")
  #   circle["x"] += 1
  # elif(circle["x"] > screen.get_width() - circle["radius"]):
  #   print("left")
  #   circle["x"] -= 1
  # else:
  #   if(circle["direction"] == "right"):
  #     circle["direction"] = "left"
  #   else:
  #     circle["direction"] = "right"