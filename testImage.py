import pygame
import time
application_width = 800
application_height = 800

application = pygame.display.set_mode((application_width, application_height))
pygame.display.set_caption("Pathfinder simple application")

courier = pygame.image.load('courier.png')
courier_x = 100
courier_y = 100
courier_vel_x = 10
courier_vel_y = 10


def main() :
    global courier_x, courier_y
    while True :
        for event in pygame.event.get():
            # untuk keluar dari game application
            if (event.type == pygame.QUIT):
                pygame.quit()
            
            application.fill((0, 0, 0))
    
            courier_x = courier_x + courier_vel_x
            courier_y = courier_y + courier_vel_y
            application.blit(courier, (courier_x, courier_y))
            pygame.display.update()
            time.sleep(1)


            


main()