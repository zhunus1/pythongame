import pygame
def move(pts):
    while pts[0]!=750:
        pts[0]+=5
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    while pts[1]>50:
        pts[0]-=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    while pts[0]>50:
        pts[0]-=1
        pts[1]+=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    while pts[1]>50:
        pts[0]+=1
        pts[1]-=1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()

def shear(pts):
    for i in range(100):
        pts[0] += 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()
    for i in range(200):
        pts[0] -= 1
        img = pygame.draw.circle(pygame.display.set_mode((800, 600)), color, pts, 100)
        pygame.display.update()
        pygame.display.flip()

surface = pygame.display.set_mode((800, 600))
color = (255, 0, 255)
pts = [350,250]
pygame.display.init()
img = pygame.draw.circle(surface, color, [375, 275], 50)
pygame.display.flip()
pygame.time.wait(1000)
img = pygame.draw.circle(surface, color, [350, 250], 100)
pygame.time.wait(1000)


shear(pts)
move([350,250])
pygame.display.flip()



