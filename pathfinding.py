from tkinter import messagebox, Tk
import pygame
import sys

application_width = 500
application_height = 500
columns = 25
rows = 25
linePixel = 2
box_size_width = application_width / columns
box_size_height = application_height / rows
box_color = (50,50,50)
grid_system = []

application = pygame.display.set_mode((application_width, application_height))
pygame.display.set_caption("Pathfinder simple application")


class Box:
    def __init__(self, positionX, positionY):
        self.x = positionX
        self.y = positionY

    def drawBox(self, windowsApp, boxColor):
        pygame.draw.rect(windowsApp, boxColor, (self.x * box_size_width, self.y *
                         box_size_height, box_size_width-linePixel, box_size_height-linePixel))


# sebelum application ditampilkan, membuat tampilan grid system berupa kotak-kotak terlebih dahulu

for i in range (columns) :
    temp_arr = []
    for j in range (rows) :
        temp_arr.append(Box(i,j))  # membuat kotak pada posisi i(posisiX),j(posisiY) di layar application
    grid_system.append(temp_arr)




def main():
    running = True
    while running:
        for event in pygame.event.get():
            # untuk keluar dari game application
            if (event.type == pygame.QUIT):
                running = False
                pygame.quit()
                sys.exit()

            application.fill((0, 0, 0))
            
            # tampilan aplikasi utama (grid sistem ditampilkan)

            for i in range(columns):
                for j in range(rows) :
                    box = grid_system[i][j]
                    box.drawBox(application, (box_color))
            pygame.display.update()


main()
