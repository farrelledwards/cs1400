# cursor.py
import pygame


class Cursor:
    def __init__(self, image, offset=[0, 0]):
        self.image = pygame.image.load(image)
        self.pos = [0, 0]
        self.offset = offset

    def update_pos(self, mouse_pos):
        self.pos = [
                mouse_pos[0] + self.offset[0],
                mouse_pos[1] + self.offset[1]
                ]

    def draw(self, screen):
        screen.blit(self.image, self.pos)
