import pygame
import random

tile=100
list_snake=[[3, 4], [4, 4], [5, 4]]
direction=[1, 0]
apples=[]
len_snake=3

pygame.init()
screen=pygame.display.set_mode((1000, 1000))
r=True
clock=pygame.time.Clock()
tick=0

def draw(x, y, color, specific):
    if specific=="rect":
        pygame.draw.rect(screen, color, (x*tile, y*tile, tile, tile))
    if specific=="circle":
        pygame.draw.circle(screen, color, (x*tile+tile//2, y*tile+tile//2), tile//2)

def check(x, y):
    if x<0 or x>9 or y<0 or y>9:
        return False
    else:
        return True

def spawn_apple():
    global apples
    x, y= random.randint(0, 9), random.randint(0, 9)
    if [x, y] not in list_snake and [x, y] not in apples:
        apples.append([x, y])
    else:
        spawn_apple()

for i in range(3):
    spawn_apple()

while r:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            r=False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w] and direction!=[0, 1]:
        direction=[0, -1]
    if keys[pygame.K_s] and direction!=[0, -1]:
        direction=[0, 1]
    if keys[pygame.K_d] and direction!=[-1, 0]:
        direction=[1, 0]
    if keys[pygame.K_a] and direction!=[1, 0]:
        direction=[-1, 0]
    
    if tick==20:
        next_x, next_y=list_snake[len(list_snake)-1][0]+direction[0], list_snake[len(list_snake)-1][1]+direction[1]
        if check(next_x, next_y) and [next_x, next_y] not in list_snake:
            list_snake.append([next_x, next_y])
        else:
            r=False
        if [next_x, next_y] in apples:
            len_snake+=1
            apples.remove([next_x, next_y])
            spawn_apple()
        if len(list_snake)>len_snake:
            list_snake.pop(0)
        tick=0
    
    screen.fill("white")

    for i in list_snake:
        draw(i[0], i[1], "green", "rect")
    
    for i in apples:
        draw(i[0], i[1], "red", "circle")
        
    pygame.display.flip()

    clock.tick(100)
    tick+=1

pygame.quit()