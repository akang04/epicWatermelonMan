import pygame

WIDTH = 800
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Epic Watermelon Man")

#load images
testAnim = []
for i in range(75):
    a = pygame.image.load('assets/frame_' + str(i) + '.gif')
    a = pygame.transform.scale(a, (WIDTH, HEIGHT)).convert()
    testAnim.append(a)

ind = 0
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    SCREEN.blit(testAnim[ind],(0,0))
    ind += 1
    if ind > 74:
        ind = 0
    
    pygame.display.update()