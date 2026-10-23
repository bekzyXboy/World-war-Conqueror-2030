import pygame
from points.point_uz import Point
from camera.camera import Camera, Map, Cube

pygame.init()

WIDTH = 1100
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((105, 105, 105))
clock = pygame.time.Clock()

# # uzb = pygame.image.load("content/maps/uzb.png").convert_alpha()
# uzb = pygame.transform.scale(uzb, (WIDTH, HEIGHT))
# Surface for the test window
test_window = pygame.Surface((WIDTH-30, HEIGHT-30))


point = Point(screen, 0, 0, 100, 100)
point.point_created(WIDTH, HEIGHT)


camera = Camera()

map = Map("content/maps/uzb.png")




run = True
while run:
    screen.fill((105, 105, 105))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(point.windows)
            for window in point.windows:
                world_x = (mx + camera.x) / camera.zoom
                world_y = (my + camera.y) / camera.zoom

                if window["rect"].collidepoint(world_x, world_y):
                    point.clicked_window = True
                    print("Window clicked!")
                    break
                else:
                    point.clicked_window = False
                    print("Window not clicked!")
        if event.type == pygame.MOUSEWHEEL:
            print(event.dict)
            if event.y > 0:
                camera.zoom_change(0.1)
                print(event.y)

            elif event.y < 0:
                camera.zoom_change(-0.1)
                print(event.y)


    camera.update()
    map.draw(screen, camera)
    point.point_draw(screen, camera)

    if point.clicked_window:
        center_tw = test_window.get_rect(center=(WIDTH // 2, HEIGHT //2))
        screen.blit(test_window, center_tw)
    
    clock.tick(60)
    pygame.display.flip()
pygame.quit()