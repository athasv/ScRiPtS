import pygame

pygame.init()

screen = pygame.display.set_mode( [640,480] )

screen.fill( [255,255,255] )

testpic = pygame.image.load("testpic.png")

screen.blit( testpic, [50,50] )
pygame.display.flip()
pygame.time.delay(2)
screen.blit( testpic, [150,50] )
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()