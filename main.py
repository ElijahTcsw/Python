import pygame
import Gridgenerator
import tilecheck
flags = 6
pygame.init()
pygame.font.init()
numberfont = pygame.font.Font("data-latin.ttf",40)
windowsurface = pygame.display.set_mode((500, 545))
pygame.display.set_caption("Minesweeper")
running = True
death = False
haswon = False
grid = Gridgenerator.creategrid(9, 9)
tile = pygame.image.load("tile.png")
flag = pygame.image.load("flag.png")
mine = pygame.image.load("mine.png")
tileempty = pygame.image.load("tileempty.png")
pygame.display.set_icon(mine)
clock = 0
while running:
    windowsurface.fill((0,0,0))
    for tiley in range(0,9):
        for tilex in range(0, 9):
            if grid[tiley][tilex] == 1:
                windowsurface.blit(tile,(tilex * 55, tiley * 55))
                if death:
                    windowsurface.blit(mine,(tilex * 55, tiley * 55))
            elif grid[tiley][tilex] == 2:
                windowsurface.blit(tileempty,(tilex * 55, tiley * 55))
                if tilecheck.touchingmine(grid, tilex, tiley) > 0:
                    numbersurface = numberfont.render(str(tilecheck.touchingmine(grid, tilex, tiley)),False,(255,255,255))
                    windowsurface.blit(numbersurface, (55 * tilex,55 * tiley))
            elif not grid[tiley][tilex]== 0:
                windowsurface.blit(flag,(tilex * 55, tiley * 55))
                if death and grid[tiley][tilex]== 3:
                    windowsurface.blit(mine,(tilex * 55, tiley * 55))
            elif grid[tiley][tilex]== 0:
                windowsurface.blit(tile,(tilex * 55, tiley * 55))
    if death:
        gameover = numberfont.render("You Died",False,(255, 0, 0))
        windowsurface.blit(gameover, (180, 220))
    if haswon:
        gameover = numberfont.render("You Won",False,(0, 255, 0))
        windowsurface.blit(gameover, (180, 220))
    if not death and not haswon:
        clock= pygame.time.get_ticks()/1000
    timer = numberfont.render(str(clock),False, (0, 0, 255))
    windowsurface.blit(timer, (0, 500))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not death and not haswon:
            mousex, mousey = pygame.mouse.get_pos()
            tilex, tiley = Gridgenerator.findtile(mousex, mousey)
            if event.button == 1:
                if grid[tiley][tilex] == 1 or grid[tiley][tilex] == 3:
                    death = True
                else:
                    if grid[tiley][tilex] == 3 or grid[tiley][tilex] == 4:
                        flags += 1
                    grid[tiley][tilex] = 2
            elif event.button == 3:
                flagresult = tilecheck.checkflags(grid, tilex, tiley, flags)
                if flagresult == 3 or flagresult == 4:
                    flags -= 1
                elif grid[tiley][tilex] == 3 or grid[tiley][tilex] == 4:
                    flags += 1
                grid[tiley][tilex] = flagresult
    haswon= tilecheck.victory(grid)
pygame.quit()