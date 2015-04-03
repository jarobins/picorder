import pygame
import random
import math

# CLASSES

class Button:
    hovered = False
    
    def __init__(self, label, img_set, pos, func):
        self.label = label
        self.img_on = img_set[1]
        self.img_off = img_set[0]
        self.pos = pos
        self.set_rect()
        self.draw()
        self.func = func
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = self.get_img()
        
    def get_img(self):
        if self.hovered:
            return self.img_on
        else:
            return self.img_off
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def do_func(self):
        self.func

class Trace:
    def __init__(self, label, color, y_pos):
        self.label = label
        self.color = color
        self.y_pos = y_pos
        self.draw_list = [(0,0),(0,0),(0,0),(0,0),
                          (0,0),(0,0),(0,0),(0,0),
                          (0,0),(0,0),(0,0),(0,0)]
        self.count = 0
            
    def draw(self, func):
        self.count += 1
        self.draw_list.append((func, self.count))
        self.draw_list = self.draw_list[1:]
        for item in reversed(range(1,12)):
            # draws a line between the data points
            # (x_pos1,
            if (self.draw_list[item][1]%size[0])-(self.draw_list[item-1][1]%size[0]) < 0:
                continue  # Skips the line that draws across the screen
            pygame.draw.line(screen, self.color,
                             (self.draw_list[item][1]%size[0],
                              self.y_pos-self.draw_list[item][0]),
                             (self.draw_list[item-1][1]%size[0],
                              self.y_pos-self.draw_list[item-1][0]))
            
        

def draw_thing():
    print "thing"
    pygame.draw.rect(screen, (255, 0, 255), (random.randint(1, 255),
                              random.randint(1, 255),
                              random.randint(1, 255),
                              random.randint(1, 255)))
    

def draw_something():
    pass

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
OK_on = pygame.image.load("./OK.png")
OK_off = pygame.image.load("./OK_on.png")
START_on = pygame.image.load("./START.png")
START_off = pygame.image.load("./START_on.png")

buttons = [Button("OK", (OK_on, OK_off), (10, 200), draw_thing()),
           Button("START", (START_on, START_off), (100, 200), draw_something())]
traces = [Trace("Heart_Beats", (255, 0, 0), 170),]

# Define Varibles
x, y, a, b = 1, 1, 2, 2
data_list = [0,0,0,0,0,0,0,-1,-3,-4,-4,-2,5,15,20,23,
             25,25,24,20,14,6,-3,-5,-6,-5,-3,-2,-1,0,0,0,0]
 
# Loop until the user clicks close button
done = False
count = 0
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print pos
            # get a list of all sprites that are under the mouse cursor
            clicked_buttons = [s for s in buttons if s.rect.collidepoint(pos)]
            if clicked_buttons:
                clicked_buttons[0].do_func
                
    # write game logic here
 
    # clear the screen before drawing
    screen.fill((255,255,255))
    
    # write draw code here
    for button in buttons:
        if button.rect.collidepoint(pygame.mouse.get_pos()):
            button.hovered = True
        else:
            button.hovered = False
        button.draw()
    for trace in traces:
        count += 1
        trace.draw(data_list[count%len(data_list)])
    # display whats drawn. this might change.
    pygame.display.update()
    # run at 20 fps
    clock.tick(48)
 
# close the window and quit
pygame.quit()
