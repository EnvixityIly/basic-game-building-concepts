import pygame
pygame.init()
screen_width,screen_height = 640,480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Hi , back or front?")

font = pygame.font.SysFont("Times new Roman", 36)
text = font.render("My first game screen", True, (255,0,0))

color = pygame.Color('blue')
x,y = 30,30
sprite_width,sprite_height = 60,60

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    

    x = 320
    y = 240
    
    screen.fill((0, 0, 0))

    screen.blit(text, (250 - text.get_width() // 2, 140 - text.get_height() // 2))

    pygame.draw.rect(screen,color,(x,y,sprite_width,sprite_height))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()