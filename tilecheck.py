def touchingmine(grid, tilex, tiley):
    foundtiles = 0
    for checkx in range(-1, 1):
        for checky in range(-1, 1):
            if grid[checkx][checky] == 1 and not (checkx == 0 and checky == 0):
                foundtiles += 1
    return foundtiles