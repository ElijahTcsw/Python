import pygame
import Gridgenerator
import tilecheck

pygame.init()
pygame.font.init()
numberfont = pygame.font.SysFont(None,40)
windowsurface = pygame.display.set_mode((500, 500))
running = True
grid = Gridgenerator.creategrid(9, 9)
while running:
    for tiley in range(0,9):
        for tilex in range(0, 9):
            if grid[tiley][tilex] == 1:
                pygame.draw.rect(windowsurface,(255, 0, 0),(tilex * 55, tiley * 55, 55, 55))
            elif grid[tiley][tilex] == 2:
                pygame.draw.rect(windowsurface,(0, 255, 0),(tilex * 55, tiley * 55, 55, 55))
                if tilecheck.touchingmine(grid, tilex, tiley) > 0:
                    numbersurface = numberfont.render(str(tilecheck.touchingmine(grid, tilex, tiley)),False,(255,255,255))
                    windowsurface.blit(numbersurface, (55 * tilex,55 * tiley))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            tilex, tiley = Gridgenerator.findtile(mousex, mousey)
            if grid[tiley][tilex] == 1:
                running = False
            else:
                grid[tiley][tilex] = 2
pygame.quit()