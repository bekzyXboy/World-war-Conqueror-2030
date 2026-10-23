import pygame

pygame.init()

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0



        self.zoom = 1.0
        self.speed = 5

        #print("Camera class worked!")

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed

    def zoom_change(self, value):
        self.zoom += value
        self.zoom = max(0.5, min(3.0, self.zoom))

        print("Zoom function worked!")

class Map:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()

    def draw(self, screen, camera):
        width = int(self.image.get_width() * camera.zoom)
        height = int(self.image.get_height() * camera.zoom)

        scaled_image = pygame.transform.scale(self.image, (width, height))

        screen.blit(scaled_image, (-camera.x, -camera.y))

class Cube:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

    def get_rect(self, camera):
        return pygame.Rect(self.x * camera.zoom - camera.x, self.y * camera.zoom - camera.y, self.width * camera.zoom, self.height * camera.zoom)

    def draw(self, screen, camera):
        # screen_x = self.x * camera.zoom - camera.x
        # screen_y = self.y * camera.zoom - camera.y

        rect = self.get_rect(camera)

        #print("Cube class worked!")
        pygame.draw.rect(screen, (31, 155, 31), rect)






