import pygame
import random
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Snake in Pygame")

grid_size = 20
box = 500/grid_size



class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0,244,0)

class Food:
    def __init__(self):
        self.x = random.randint(0, grid_size)
        self.y= random.randint(0, grid_size)

food = Food()

snake_body = [Snake(10,10), Snake(11,10)]

run = True
fps = 1000/10
d = "right"

while run:
    pygame.time.delay(int(fps))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if d == "down":
         snake_body.insert(0, Snake((snake_body[0].x), snake_body[0].y + 1))
    if d == "up":
         snake_body.insert(0, Snake((snake_body[0].x), snake_body[0].y - 1))
    if d == "right":
        snake_body.insert(0, Snake((snake_body[0].x)+1, snake_body[0].y))
    if d == "left":
        snake_body.insert(0, Snake((snake_body[0].x)-1, snake_body[0].y))
    
    if snake_body[0].x == food.x and snake_body[0].y == food.y:
        food = Food()
    else:
        snake_body.pop()
   
    if keys[pygame.K_DOWN]:
        d = "down"

    if keys[pygame.K_UP]:
        d = "up"

    
    if keys[pygame.K_LEFT]:
        d = "left"

    if keys[pygame.K_RIGHT]:
        d = "right"
    win.fill((51, 51, 51))
            
    for i in range(len(snake_body)):
        if i == 0:
            pygame.draw.rect(win, (0,125, 0), (snake_body[i].x*box, box*snake_body[i].y, 20,20))
        else:
            pygame.draw.rect(win, (0,255, 0), (snake_body[i].x*box, box*snake_body[i].y, 20,20))
        if snake_body[i].x < 0:
            snake_body[i].x = 20
        if snake_body[i].y< 0:
            snake_body[i].y = 20
        if snake_body[i].x > 20:
            snake_body[i].x = 0
        if snake_body[i].y > 20:
            snake_body[i].y = 0
    pygame.draw.rect(win, (255,0, 0), (food.x*box, box*food.y, 20,20))

    pygame.display.update()
    

pygame.quit()
