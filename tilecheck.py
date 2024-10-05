
def checkflags(grid, tilex, tiley):
    if grid[tiley][tilex] == 1:
        return 3
    elif grid[tiley][tilex] == 0:
        return 4
    elif grid[tiley][tilex] == 3:
        return 1
    elif grid[tiley][tilex] == 4:
        return 0
    elif grid[tiley][tilex] == 2:
        return 2
def touchingmine(grid, tilex, tiley):
    foundtiles = 0
    for checkx in range(-1, 2):
        finalx = tilex+ checkx
        for checky in range(-1, 2):
            finaly= tiley + checky
            if (finalx >= 0 and finalx< 9 and finaly >= 0 and finaly< 9):
                if grid[finaly][finalx] == 1:
                    foundtiles += 1
    return foundtiles