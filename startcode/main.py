import pygame, sys
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Supper Paint")
filename = "Image"
window.fill((255, 255, 255))
color = 0
width = 10
colors = [(0,0,0),(206,206,206),(255,0,0),(255,150,0),(255,222,89),(125, 218, 88),(0,255,255),(0,0,255),(150,0,255),(255, 236, 161)]


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if pygame.mouse.get_pressed() == (True,False,False):
            pygame.draw.circle(window, colors[color], pygame.mouse.get_pos(), width)

        if pygame.mouse.get_pressed() == (False,False,True):
            pygame.draw.circle(window, (255,255,255), pygame.mouse.get_pos(), width)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if color == len(colors)-1:
                    color = -1
                color = color + 1
                pygame.draw.line(window, color, (0, 0), (0, 1000), 10)

            if event.key == pygame.K_UP:
                width += 5

            if event.key == pygame.K_DOWN:
                width -= 5

            if event.key == pygame.K_s:
                pygame.image.save(window, filename + ".jpg")


    pygame.display.update()
