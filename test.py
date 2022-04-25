from http.client import CONTINUE
from tkinter import messagebox, Tk
import pygame
import sys
import random
application_width = 800
application_height = 800

columns = 10
rows = 10

linePixel = 2
box_size_width = application_width // columns
box_size_height = application_height // rows
box_blank_color = (50,50,50)
box_start_color = (0,200,200)
box_wall_color = (90,90,90)
box_target_color = (200,200,0)


grid_system = []

application = pygame.display.set_mode((application_width, application_height))
pygame.display.set_caption("Pathfinder simple application")


class Box:
    def __init__(self, positionX, positionY):
        self.x = positionX
        self.y = positionY
        self.start = False
        self.target = False
        self.wall = False

    def drawBox(self, windowsApp, boxColor):
        pygame.draw.rect(windowsApp, boxColor, (self.x * box_size_width, self.y *
                         box_size_height, box_size_width-linePixel, box_size_height-linePixel))


# sebelum application ditampilkan, membuat tampilan grid system berupa kotak-kotak terlebih dahulu

for i in range (columns) :
    temp_arr = []
    for j in range (rows) :
        temp_arr.append(Box(i,j))  # membuat kotak pada posisi i(posisiX),j(posisiY) di layar application
    grid_system.append(temp_arr)

#membuat wall_box
xWall = random.randint(0,columns-1)
yWall =random.randint(0,rows-1)
for i in range (25) :
        xWall = random.randint(0,columns-1)
        yWall =random.randint(0,rows-1)
        if(xWall != 0 and yWall != 0) :
            wall_box = grid_system[xWall][yWall]
            wall_box.wall = True
        else :
            continue

        
            
        

# posisi start box
xStart = random.randint(0,columns-1)
yStart = random.randint(0,rows//2.5)
if(grid_system[xStart][yStart].wall != True and grid_system[xStart][yStart].target != True) :
    start_box_index = grid_system[xStart][yStart]
    start_box_index.start = True
    # start_box_index.visited = True
else :
    print("start to 0,0")
    start_box_index = grid_system[0][0]
    start_box_index.start = True

# posisi target box
xTarget = random.randint(4,columns-1)
yTarget = random.randint(4,rows-1)

if(grid_system[xTarget][yTarget].wall != True and grid_system[xTarget][yTarget].start != True) :
    target_box_index = grid_system[xTarget][yTarget]
    target_box_index.target = True
    target_box_set = True
else :
    print("target to rows,columns")
    target_box_index = grid_system[rows-1][columns-1]
    target_box_index.target = True
    target_box_set = True

# posisi target variable nya ==> target_box_index


def main():
    running = True

    begin_search = False # untuk syarat agar algoritma akan dimulai
    target_box_set = False # untuk syarat agar target hanya boleh satu

    while running:
        for event in pygame.event.get():
            # untuk keluar dari game application
            if (event.type == pygame.QUIT):
                running = False
                pygame.quit()
                sys.exit()
            # penggunaan mouse untuk menentukan posisi target dan membuat wall maze
            elif (event.type == pygame.MOUSEMOTION) :
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                # klik kiri untuk draw wall
                if (event.buttons[0]) : # buttons[0] = left mouse click
                    indexMouseX = x // box_size_width
                    indexMouseY = y // box_size_width
                    grid_system[indexMouseX][indexMouseY].wall = True

                # klik kanan untuk set target finish
                if (event.buttons[2] and not target_box_set) : # buttons[2] = right mouse click
                    indexMouseX = x // box_size_width
                    indexMouseY = y // box_size_width
                    target_box_index = grid_system[indexMouseX][indexMouseY]
                    target_box_index.target = True
                    target_box_set = True

            # memulai algoritma dengan mengklik tombol enter
            if (event.type == pygame.KEYDOWN and target_box_set) :
                begin_search = True




            application.fill((0, 0, 0))
            
            # tampilan aplikasi utama (grid sistem ditampilkan)

            for i in range(columns):
                for j in range(rows) :
                    box = grid_system[i][j]
                    box.drawBox(application, (box_blank_color))

                    if(box.start) :
                        box.drawBox(application, (box_start_color))
                    if(box.wall) :
                        box.drawBox(application, (box_wall_color))
                    if(box.target) :
                        box.drawBox(application, (box_target_color))
                    

            pygame.display.flip()


main()