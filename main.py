import pygame
import random

pygame.init() #pygame is a class finction so it need to be initiated
wt=800
ht=600
car_wt=50
car_ht=100
disp=pygame.display.set_mode((wt,ht))
pygame.display.set_caption('CAR RACE')
clk=pygame.time.Clock()
car=pygame.image.load('car.jpg')
enemy=pygame.image.load('enemy.jpg')

def cardisp(car,x,y):
    disp.blit(car,(x,y))
def road(y):
    pygame.draw.rect(disp,(0,0,255),[190,y-200,20,100])
    pygame.draw.rect(disp,(0,0,255),[190,y,20,100])
    pygame.draw.rect(disp,(0,0,255),[190,y+200,20,100])
    pygame.draw.rect(disp,(0,0,255),[190,y+400,20,100])
    pygame.draw.rect(disp,(0,0,255),[590,y-200,20,100])
    pygame.draw.rect(disp,(0,0,255),[590,y,20,100])
    pygame.draw.rect(disp,(0,0,255),[590,y+200,20,100])
    pygame.draw.rect(disp,(0,0,255),[590,y+400,20,100])
    
crashed = False
enemy_x=random.randrange(0,750)
enemy_y=-100
speed=10
car_x=375
car_y=500
x_change=0
y_change=0
road_y=0

while not crashed :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-5
            elif event.key==pygame.K_RIGHT:
                x_change=+5
            if event.key==pygame.K_UP:
                y_change=-5
            elif event.key==pygame.K_DOWN:
                y_change=+5
        if event.type==pygame.KEYUP:
            x_change=0
            y_change=0

    disp.fill((255,225,255))
    road(road_y)
    road_y+=speed-1
    if road_y>=200:
        road_y=0
    #disp.blit(car,(400,500))
    #disp.blit(enemy,(400,0)
    car_x+=x_change
    car_y+=y_change
    if car_x<=0 or car_x>=750:
        car_x-=x_change
    if car_y<=0 or car_y>=500:
        car_y-=y_change
        
    cardisp(car,car_x,car_y)
    enemy_y+=speed
    cardisp(enemy,enemy_x,enemy_y)
    if enemy_y>=ht:
        enemy_y=-100
        enemy_x=random.randrange(0,750)
    #car crash
    if car_y<=(enemy_y+100) and (car_y+100)>=enemy_y:
        if (enemy_x+50)>=car_x and enemy_x<=(car_x+50):
            crashed=True
            print("CRASH")
            pygame.quit()
            quit()
    
    pygame.display.update()
    clk.tick(60)

