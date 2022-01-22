
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
rows = 50
openset = []
closedset = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 800/cols 
h = 800/rows 
camefrom = [] 

for i in range(cols): 
    grid[i] = [0 for i in range(cols)]

for i in range(cols):
    for j in range(rows):
        grid[i][j].show((255,255,255))


    


