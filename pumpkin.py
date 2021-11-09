import pygame
import math
pygame.init()

doExit = False

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Punkin")


while not doExit:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 100, 0), (120, 180, 25, 110))
    pygame.draw.ellipse(screen, (255, 140, 0), (35, 255, 200, 200))
    pygame.draw.arc(screen, (0,0,0), (105,310,30,20), math.pi, math.pi*2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
    pygame.draw.arc(screen, (0,0,0), (95,290,20,20), 0, math.pi, 5)
    pygame.draw.arc(screen, (0,0,0), (120,290,20,20), 0, math.pi, 5)
    
    pygame.draw.rect(screen, (0, 100, 0), (120, -20, 25, 110))
    pygame.draw.ellipse(screen, (255, 0, 0), (35, 25, 200, 200))
    pygame.draw.arc(screen, (0,0,0), (105,95,30,20), math.pi, math.pi*2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
    pygame.draw.arc(screen, (0,0,0), (95,75,20,20), 0, math.pi, 5)
    pygame.draw.arc(screen, (0,0,0), (120,75,20,20), 0, math.pi, 5)
    
    pygame.draw.rect(screen, (0, 100, 0), (340, -20, 25, 110))
    pygame.draw.ellipse(screen, (0, 0, 255), (255, 25, 200, 200))
    pygame.draw.arc(screen, (0,0,0), (325,95,30,20), math.pi, math.pi*2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
    pygame.draw.arc(screen, (0,0,0), (315,75,20,20), 0, math.pi, 5)
    pygame.draw.arc(screen, (0,0,0), (340,75,20,20), 0, math.pi, 5)
    
    pygame.draw.rect(screen, (0, 100, 0), (370, 340, 110, 25))
    pygame.draw.ellipse(screen, (255, 192, 203), (255, 255, 200, 200))
    pygame.draw.arc(screen, (0,0,0), (380,335,30,20), math.pi/2, math.pi*3/2, 5) #(185, 400) is the top left corner of the box that the arc is drawn in
    pygame.draw.arc(screen, (0,0,0), (400,320,20,20), math.pi*3/2 , math.pi/2 ,5)
    pygame.draw.arc(screen, (0,0,0), (400,350,20,20), math.pi *3/2 , math.pi/2 ,5)
    
    pygame.display.flip()

pygame.quit()
