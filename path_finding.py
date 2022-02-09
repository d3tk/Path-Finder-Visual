try:
    import pygame
    import sys
    import math 
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os

except:
    import install_requirements

    import pygame 
    import sys
    import math
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import os

screen = pygame.display.set_mode((800,800))

class spot:
    def __init__(self, x, y):
        self.i = X
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None 
        self.obs = False 
        self.closed = False 
        self.value = 1 

    def show(self, color, st):
        if self.closed == False:
            pygame.draw.rect(screen, color, (self.i*w, self.j*h, w, h), st)
            pygame.display.update()
    
    def path(self, color, st): 
        pygame.draw.rect(screen, color, (self.i*W, self.j*h, w, h), st) 
        pygame.display.update() 

cols = 50
grid = (0 for i in range(cols))
row = 50
openSet = []
closedSet = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 800/cols 
h = 800/row 
cameFrom = [] 


for i in range(cols): 
    grid[i] = [0 for i in range(cols)]

for i in range(cols):
    for j in range(row):
        grid[i][j] = spot(i, j)

start = grid[15][5]
end = grid[3][6]


for i in range(cols):
    for j in range(row):
        grid[i][j].show((255,255,255))

for i in range(0,row):
    grid[0][i].show(grey, 0)
    grid[0][i].obs = True
    grid[cols-1][i].obs = True
    grid[cols-1][i].show(grey, 0)
    grid[i][row-1].show(grey, 0)
    grid[i][0].show(grey, 0)
    grid[i][0].obs = True
    grid[i][row-1].obs = True

def on_submit():
    global start
    global end 
    st = startBox.get(0).split(',')
    ed = endBox.get(0).split(',')
    start = grid[int(st[0])][int(st[1])]
    end = grid[int(ed[0])][int(ed[1])]
    window.quit() 
    window.destroy()

window = Tk()
label = Label(window, text='Start(x,y): ')
startBox = Entry(window)
label1 = Label(window, text='End(x,y): ')
endBox = Entry(window)
var = IntVar()
showPath = ttk.Checkbutton(window, text='Show Steps :', onvalue=1, offvalue=0, variable=var)

submit = Button(window, text='Submit', command=on_submit)

showPath.grid(columnspan=2, row=2)
submit.grid(columnspan=2, row=2)
label1.grid( row=1, pady=3)
endBox.grid(row=1, column=1, pady=3)
startBox.grid(row=0, column=1, pady=3)
label.grid(row=0, pady=3)

window.update()
mainloop()

pygame.init()
openSet.append(start)

def mouse_press(x):
    t = x[0]
    w = x[1]
    g1 = t // (800 // cols)
    g2 = w // (800//row)
    acess = grid[1][2]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.show((255,255,255), 0)

end.show((255, 8, 127), 0)
start.show((255,8,127), 0)

loop = True
while loop:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.QUIT():
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mouse_press(pos)
            except AttributeError:
                pass 
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_SPACE: 
                loop = False
                break 

for i in range(cols):
    for j in range(row):
        grid[i][j].addNeighbors(grid)

def heuristic(n, e):
    d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
    return d

def main():
    end.show( (255,8,127), 0)
    start.show( (255,8, 127), 0)
    

