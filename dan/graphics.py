import pygame
from pygame import gfxdraw

# must be in a ratio of 2:1
windowWidth = 1536
windowHeight = 768

# initialise the font and some of the text that will be displayed
# i've chosen arial because i can assume that all windows machines have it and anyone who uses linux can install it (as i have done). i dont care about mac lol
pygame.font.init()
fontLarge = pygame.font.SysFont("Arial", 32)
fontSmall = pygame.font.SysFont("Arial", 24)
textTitle = fontLarge.render("Circle Packing Challenge", True, (0,0,0))
textCircleCount = fontSmall.render("Circles to pack: ", True, (0,0,0))
textDiameter = fontSmall.render("Outer circle diameter: ", True, (0,0,0))

# create a window and fill it with white
screen = pygame.display.set_mode((windowWidth, windowHeight))
screen.fill((255,255,255))

# render the circles, the names above and the "Outer circle diameter: " thing for each person
names = ["Ben", "Dan", "Luca"]
for circle in range(0,len(names),1):
    circleX = windowWidth//6 + circle*windowWidth//3
    textName = fontSmall.render(names[circle], True, (0,0,0))
    screen.blit(textName, (circleX - textName.get_width()//2, windowHeight - windowWidth//3 - textName.get_height()*4))
    screen.blit(textDiameter, (circleX - textDiameter.get_width()//2, windowHeight - windowWidth//3 - textDiameter.get_height()*3))
    # the circle is drawn twice because there's no thickness argument for anti-aliased circles for some reason
    pygame.gfxdraw.aacircle(screen, circleX, (windowHeight // 3 * 2), (windowWidth // 6), (0,0,0))
    pygame.gfxdraw.aacircle(screen, circleX, (windowHeight // 3 * 2), (windowWidth // 6 - 1), (0,0,0))

# render the title and "Circles to pack: "
screen.blit(textTitle, (windowWidth//2 - textTitle.get_width()//2,textTitle.get_height() * 0.5))
screen.blit(textCircleCount, (windowWidth//2 - textTitle.get_width()//2,textTitle.get_height() * 2))

# update the screen
pygame.display.flip()

# running loop (so it doesnt immediately close)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()