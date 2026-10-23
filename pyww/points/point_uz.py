import pygame
from settings import FONT
from camera.camera import Camera

class Point:
    def __init__(self, screen,  x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.screen = screen
        self.windows = []
        self.clicked_window = False
        self.clicked = False
        self.names = ["Navoi", "Toshkent", "Samarqand", "Buxoro", "Farg'ona", "Andijon", "Xorazm"]

    # def get_rect(self, camera):
    #     return pygame.Rect(self.x * camera.zoom - camera.x, self.y * camera.zoom - camera.y, self.width * camera.zoom, self.height * camera.zoom)


    def point_created(self, WIDTH, HEIGHT):
        for x in range(3):
            for y in range(3):
                index = len(self.windows)
                self.windows.append({"rect": pygame.Rect(10 + x * 50, y * 50, 40, 40), "name": self.names[index] if index < len(self.names) else ""})
                # pygame.draw.rect(self.screen, (55, 155, 55), self.windows[-1], 0, 5)

                self.windows[0]["rect"].x = WIDTH / 4 - 75
                self.windows[0]["rect"].y = HEIGHT / 4 - 75

                if len(self.windows) > 6: 
                    #Navoi
                    self.windows[1]["rect"].x = WIDTH / 2 
                    self.windows[1]["rect"].y = HEIGHT / 2 - 75
                
                    #Toshkent
                    self.windows[2]["rect"].x = WIDTH / 4 * 3 + 35
                    self.windows[2]["rect"].y = HEIGHT / 2
                    #4
                    self.windows[3]["rect"].x = WIDTH / 5 * 3 + 35
                    self.windows[3]["rect"].y = HEIGHT / 3 + 100  
                    #5
                    self.windows[4]["rect"].x = WIDTH / 2 * 3 + 35
                    self.windows[4]["rect"].y = HEIGHT / 2
                    #6
                    self.windows[5]["rect"].x = WIDTH / 4 * 1 + 35
                    self.windows[5]["rect"].y = HEIGHT / 2  
                    #7
                    self.windows[6]["rect"].x = WIDTH / 4 * 3 + 35
                    self.windows[6]["rect"].y = HEIGHT / 3

    def point_draw(self, screen, camera):
        for window in self.windows:
            text = FONT.render(window["name"], True, (0, 0, 0))

            screen_x = window["rect"].x * camera.zoom - camera.x
            screen_y = window["rect"].y *camera.zoom - camera.y

            width =  window["rect"].width  * camera.zoom
            height = window["rect"].height * camera.zoom

            rect = pygame.Rect(screen_x, screen_y, width, height)

            pygame.draw.rect(self.screen, (31 + window["rect"].x // 10, 11, 3 + window["rect"].x // 10), rect, 0, 5)
            self.screen.blit(text, (screen_x + 5, screen_y + 5))



            #print("Cube class worked!")
            # pygame.draw.rect(screen, (31, 155, 31), rect)