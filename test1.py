from tkinter import messagebox, Tk
import pygame
import sys
import time 
import random
window_width = 400
window_height = 400


window = pygame.display.set_mode((window_width, window_height))

columns = 10
rows = 10

box_width = window_width // columns
box_height = window_height // rows

grid = []
queue = []
path = []


class Box:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.start = False
        self.wall = False
        self.target = False
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.prior = None

    def draw(self, win, color):
        pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width-2, box_height-2))

    def draw_car(self, win, color):
        
        pygame.draw.polygon(win, color, [(50, 100), (100, 50), (150, 100)])
    
    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])


# Create Grid
for i in range(columns):
    arr = []
    for j in range(rows):
        arr.append(Box(i, j))
    grid.append(arr)

# Set Neighbours
for i in range(columns):
    for j in range(rows):
        grid[i][j].set_neighbours()

start_box = grid[random.randint(0,columns-1)][random.randint(0,rows//2.5)]
start_box.start = True
start_box.visited = True
queue.append(start_box)
road_path = []


def main():
    begin_search = False
    target_box_set = False

    target_box = grid[random.randint(4,columns-1)][random.randint(4,rows-1)]
    target_box.target = True
    target_box_set = True
    searching = True
    # target_box = None
    pathI = 0

    for i in range (10) :
        wall_box = grid[random.randint(0,columns-1)][random.randint(0,rows-1)]
        wall_box.wall = True

    while True:
        for event in pygame.event.get():
            # Quit Window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Mouse Controls
            # elif event.type == pygame.MOUSEMOTION:
            #     x = pygame.mouse.get_pos()[0]
            #     y = pygame.mouse.get_pos()[1]
            #     # Draw Wall
            #     if event.buttons[0]:
            #         i = x // box_width
            #         j = y // box_height
                    
                # # Set Target
                # if event.buttons[2] and not target_box_set:
                #     i = x // box_width
                #     j = y // box_height
                    
                #     target_box.target = True
                #     target_box_set = True
            # Start Algorithm
            if event.type == pygame.KEYDOWN and target_box_set:
                begin_search = True

        if begin_search:
            if len(queue) > 0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            queue.append(neighbour)
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There is no solution!")
                    searching = False
        
        window.fill((0, 0, 0))

        for i in range(columns):
            for j in range(rows):
                box = grid[i][j]
                box.draw(window, (100, 100, 100))

                if box.queued:
                    box.draw(window, (200, 0, 0))
                if box.visited:
                    box.draw(window, (0, 200, 0))
                if box in path:
                    box.draw(window, (125, 100, 100))
                    road_path.append([i,j])


                if box.start:
                    box.draw(window, (0, 200, 200))
                if box.wall:
                    box.draw(window, (10, 10, 10))
                if box.target:
                    box.draw(window, (200, 200, 0))

        if searching == False :
            print(road_path)
            for x in range (len(road_path)) :
                grid[road_path[x-1][0]][road_path[x-1][1]].draw(window , (100,100,100))
                grid[road_path[x][0]][road_path[x][1]].draw_car(window , (255,90,90))
                if(x+1 < len(road_path)) :
                    grid[road_path[x+1][0]][road_path[x+1][1]].draw(window , (100,100,100))
                pygame.display.flip()
                time.sleep(0.3)
                print("item ke -",x," path_box x: ", road_path[x][0], " path box y : ", road_path[x][1])
            road_path_message = " ==> ".join([str(item) for item in road_path])

            Tk().wm_withdraw()
            messagebox.showinfo("The Solution", road_path_message)
            break
            
        pygame.display.flip()




main()

