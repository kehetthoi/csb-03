import pygame
pygame.init
screen_width=600
screen_height=600
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game ngu")
ball_image=pygame.image.load('assets/ball.png')
paddle_image=pygame.image.load('assets/paddle.png')
ball_x=screen_width/2
ball_y=screen_height/2
player1_x=5
player1_y=screen_height/2
player2_x=595
player2_y=screen_height/2
w_pressed=False
s_pressed=False
up_pressed=False
down_pressed=False
pygame.time.Clock()
fps=60
loop=True
event=pygame.event.get
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
               loop = False
            elif event.key == pygame.K_SPACE:
                print("Spacebar pressed!")


