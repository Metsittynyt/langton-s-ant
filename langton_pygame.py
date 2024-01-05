######    LANGTON'S ANT    ################################

##########   RULES  #######################################
# 1) If the ant is on a black cell, it turns 90° clockwise#
#    (=right) and moves forward one cell.                 #
# 2) If the ant is on a white cell, it turns 90° counter- #
#    clockwise (=left) and moves forward one cell.        #
# 3) The color of the cell changes when ant leaves it.    #
###########################################################

import pygame, sys, time

# background: white, gridcolor: black
# turned box: gray, ant color: red
background = (255, 255, 255)
turn = (100, 100, 100)
gridcolor = (0, 0, 0)
antColor = (255, 0, 0)
# cell size and amount
cellSize = 30
numOfCells = 20
# ant's speed
fps = 1.0 / 10

# left, right, up, down
directions = (
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
    )

def langton():
    pygame.init()

    # Caption
    pygame.display.set_caption("Langton's Ant")

    # Screensize
    size = width, height = numOfCells * cellSize, numOfCells *cellSize

    # Screen
    screen = pygame.display.set_mode(size)
    screen.fill(background)
    pygame.display.flip()

    # Add grid
    for i in range(1, numOfCells):
        pygame.draw.line(screen, gridcolor, (i * cellSize, 1), (i * cellSize, numOfCells * cellSize), 2)
        pygame.draw.line(screen, gridcolor, (1, i * cellSize), (numOfCells * cellSize, i * cellSize), 2)
    pygame.display.flip()

    # ant starts from the middle
    antX, antY = numOfCells / 2, numOfCells / 2
    antDirection = 0
    board = [ [False] * numOfCells for x in range(numOfCells) ]
    
    while True:

        if board[int(antX)][int(antY)]:
            board[ int(antX) ][ int(antY) ] = False
            # flip to white
            screen.fill(background, pygame.Rect(antX * cellSize + 2, antY * cellSize + 2, cellSize -2, cellSize -2))
            # next direction
            antDirection = (antDirection + 1) % 4
        else:
            board[ int(antX) ][ int(antY) ] = True
            # flip to grey
            screen.fill(turn, pygame.Rect(antX * cellSize + 2, antY * cellSize + 2, cellSize -2, cellSize -2))
            # next direction
            antDirection = (antDirection + 3) % 4

        # move ant
        antX = (antX + directions[antDirection][0]) % numOfCells
        antY = (antY + directions[antDirection][1]) % numOfCells

        # mark ant
        screen.fill(antColor, pygame.Rect(antX * cellSize + 2, antY * cellSize + 2, cellSize -2, cellSize -2))
        
        # update display and wait some time
        pygame.display.flip()
        time.sleep(fps)
    
langton()
