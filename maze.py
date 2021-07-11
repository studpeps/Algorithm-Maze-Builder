import pygame
import os
import sys

from Algorithms.nodes.nodes import *
from Algorithms.nodes.button import *
from Algorithms.prims import prims
from Algorithms.astar import astar
from Algorithms.dijkstra import dijkstra
from Algorithms.kruskal import kruskal
from Algorithms.sidewinder import sidewinder
from Algorithms.recursive_backtracking import backtrack
from Algorithms.ellers import ellers
from Algorithms.aldous_broder import aldous
from Algorithms.wilson import wilson
from Algorithms.hunt_and_kill import hunt
from Algorithms.growing_tree import tree
from Algorithms.binary_tree import binary
from Algorithms.recursive_division import division

FILEPATH = os.getcwd()

WIDTH = 1550
COLUMNS = 99

HEIGHT = 700
ROWS = 49

GREY = (128,128,128)
WHITE = (255,255,255)

stage = 3
rainbow = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (150, 0, 255)]
col1, col2, col3 = rainbow[stage]
count = 6

MODE = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualiser")
pygame.display.set_icon(pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'icon.png')))

def make_grid():
    grid = []
    gap = WIDTH // COLUMNS
    for i in range(ROWS):
        grid.append([])
        for j in range(COLUMNS):
            node = Nodes(i, j, gap, ROWS, COLUMNS, MODE)
            grid[i].append(node)
    return grid

def draw_grid(win):
    gap = WIDTH // COLUMNS
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i*gap), (WIDTH, i*gap))
    for i in range(COLUMNS):
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, HEIGHT))

def draw(win, grid, t, w=''):
    for row in grid:
        for node in row:
                node.draw(win)
                
    if t:
        draw_grid(win)
    pygame.display.update()

def get_clicked(pos):
    gap = WIDTH // COLUMNS
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col

def main():
    global MODE
    grid = make_grid()
    pygame.init()
    start = None
    end = None
    togglegrid = True

    run = True
    started = False
    sim = False

    while run:
        if not started:
            draw(WIN, grid, togglegrid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True 

            if pygame.mouse.get_pressed()[0] and not started:
                if sim:
                    start = None
                    end = None
                    grid = make_grid()
                    pygame.display.set_caption("Visualiser: Edit")
                    sim = False
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos)
                spot = grid[col][row]
                if not start and spot != end:
                    start = spot
                    start.make_start()
            
                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()
                   
            elif pygame.mouse.get_pressed()[2]and not started:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos)
                spot = grid[col][row] 
                spot.reset()

                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and not started and start and end:
                    started = True
                    pygame.display.set_caption("Visualiser: A * Algorithm")
                    astar(lambda : draw(WIN, grid, togglegrid), grid, start, end, MODE)
                    started = False
                    sim = True

                if event.key == pygame.K_x and not started and start and end:
                    started = True
                    pygame.display.set_caption("Visualiser: Dijkstra Algorithm")
                    dijkstra(lambda : draw(WIN, grid, togglegrid), grid, start, end, MODE)
                    started = False
                    sim = True
                    

                if event.key == pygame.K_4 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Recursive backtracking Algorithm")
                    run = backtrack(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_2 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Kruskal's Algorithm")
                    run = kruskal(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_3 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Sidewinder Algorithm")
                    run = sidewinder(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_1 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Prims's Algorithm")
                    run = prims(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_q and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Ellers's Algorithm")
                    run = ellers(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_5 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Aldous Broder Algorithm(VERY SLOW!!!)")
                    run = aldous(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_0 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Wilson's Algorithm")
                    run = wilson(lambda : draw(WIN, grid, togglegrid, 'wil'), grid, MODE)
                    started = False
                
                if event.key == pygame.K_6 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Hunt and Kill algorithm")
                    run = hunt(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False

                if event.key == pygame.K_7 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Growing Tree algorithm")
                    run = tree(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_8 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Binary Tree algorithm")
                    run = binary(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False
                
                if event.key == pygame.K_9 and not started and not start and not end:
                    started = True
                    pygame.display.set_caption("Visualiser: Recursive Division algorithm")
                    run = division(lambda : draw(WIN, grid, togglegrid), grid, MODE)
                    started = False


                if event.key == pygame.K_BACKSPACE:
                    start = None
                    end = None
                    grid = make_grid()
                    pygame.display.set_caption("Visualiser: Edit")
                    sim = False
                
                if event.key == pygame.K_ESCAPE:
                    pygame.display.set_caption("Visualiser: Main Page")
                    return False

                if event.key == pygame.K_TAB:
                    togglegrid = not togglegrid
                
                if event.key == pygame.K_h:
                    helppage()

        pygame.display.set_caption("Visualiser: Edit")
    return True

def invert(color):
    a, b, c = color
    return (abs(255 - a), abs(255 - b), abs(255 - c))


def helppage(k=False):
    if k:
        return
    pygame.init()
    Quit = False
    inv = False

    background1 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help1.png'))

    nextpage = button((0, 0, 0), 1300, 350, 75, 100, FILEPATH, (0, 0, 0), text='>')
    while not Quit:
        if k:
            return
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if nextpage.isOver(pos):
                        k = helppage2()
                        continue

            if event.type == pygame.MOUSEMOTION:
                if nextpage.isOver(pos):
                    inv = True
                else:
                    inv = False
        WIN.blit(background1, (0, 0))
        fillhelp(inv, nextpage)
    
def helppage2():
    pygame.init()
    Quit = False
    inv = False
    inv1 = False
    page = 1

    background2 = pygame.image.load(os.path.join(FILEPATH, 'Fonts', 'Help2.png'))
   
    prevpage = button((0, 0, 0), 1300, 350, 75, 100, FILEPATH, (0, 0, 0), text='<')
    while not Quit:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if prevpage.isOver(pos):
                        page = 1
                        helppage()
                        
            if event.type == pygame.MOUSEMOTION:
                if prevpage.isOver(pos):
                    inv1 = True
                else:
                    inv1 = False
        WIN.blit(background2, (0, 0))
        fillhelp(inv1, prevpage)
    
def fillhelp(inv2, btn2):
    color = WHITE

    if inv2:
        btn2.textcolor = invert(color)
        btn2.color = color
    else:
        btn2.textcolor = color
        btn2.color = invert(color)
    btn2.draw(WIN, btn2.textcolor)  


    pygame.display.update()


if __name__ == "__main__":
    main()