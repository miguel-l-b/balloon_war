from tkinter import constants
import pygame

class Frame():
  pass

class SpriteSheet(object):
    def __init__(self, file_name, width, height):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.__width = width
        self.__height = height

    def get_image(self, x, y):
        image = pygame.Surface([self.__width, self.__height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, self.__width, self.__height))
        image.set_colorkey(constants.WHITE)
        return image