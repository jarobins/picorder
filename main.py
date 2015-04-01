import pygame
import random

# CLASSES

class Button:
    hovered = False
    
    def __init__(self, label, img_set, pos):
        self.label = label
        self.img_hov = img_set[1]
        self.img_off = img_set[0]
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = self.get_img()
        
    def get_img(self):
        if self.hovered:
            return self.img_clik
        else:
            return self.img_off
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos    

 
# initialize game engine
pygame.init()
# set screen width/height and caption
size = [320, 240]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption('My Game')
# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Font 
myfont = pygame.font.SysFont("monospace", 15)

# Sprites
OK_hov = pygame.image.load("./OK.png")
OK_off = pygame.image.load("./START.png")

buttons = [Button("OK", (OK_hov, OK_off), (10, 10)),
           Button("START", (OK_off, OK_hov), (10, 40)),]
# Define Varibles
x, y, a, b = 1, 1, 2, 2
 
# Loop until the user clicks close button
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print pos
            # get a list of all sprites that are under the mouse cursor
            clicked_buttons = [s for s in buttons if s.rect.collidepoint(pos)]
            if clicked_buttons:
                print clicked_buttons[0].label
                
    # write game logic here
 
    # clear the screen before drawing
    screen.fill((255,255,255))
    
    # write draw code here
    for button in buttons:
        button.draw()
    # display whats drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(48)
 
# close the window and quit
pygame.quit()
