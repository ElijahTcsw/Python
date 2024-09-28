import random
def creategrid(width,height):
    grid = []
    for collumn in range(0,height):
        section = []
        for tile in range (0, width):
            section.append(0)
        grid.append(section)
    for mine in range(0,6): 
        while True:
            minex = random.randrange(0, 9)
            miney = random.randrange(0, 9)
            if grid[minex][miney] == 0:
                grid[miney][minex] = 1
                break
    return grid
def get1Dtile(x):
    for tile in range(0,9):
        screentile = 55 * tile
        if screentile < x and screentile + 55 > x:
            return tile
def findtile(mousex, mousey):
    return (get1Dtile(mousex),get1Dtile(mousey))