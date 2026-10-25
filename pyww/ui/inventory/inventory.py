import pygame

class Inventory:
    def __init__(self, screen, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.items = [1, 2, 3]
        self.selected_item = None

    # def add_item(self, item):
    #     self.items.append(item)

    def draw(self, camera):
        for item in self.items:
            

            rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)

            print("Inventory drawing!")