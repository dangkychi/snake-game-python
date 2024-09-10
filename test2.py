# importing libraries
import pygame
import time
import random
import sys
import turtle

snake_speed = 15

# Window size
window_x=720
window_y=480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('snake hunting')
icon=pygame.image.load(r'images\icon1.png')
pygame.display.set_icon(icon)
bg=pygame.image.load(r'images\bg1.png')
bg=pygame.transform.scale2x(bg)
bgend=pygame.image.load(r'images\bggameover.jfif')

screen = pygame.display.set_mode((window_x,window_y))

# defining snake default position
snake_position = [window_x/2-10, window_y/2]

# defining first 4 blocks of snake body
snake_body = [[window_x/2-10, window_y/2],
			[window_x/2-20, window_y/2],
			[window_x/2-30, window_y/2],
			[window_x/2-40, window_y/2]
			]

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# FPS (frames per second) controller
fps = pygame.time.Clock()

# displaying Score function
def show_score(choice, color, font, size):

	# creating font object score_font
	score_font = pygame.font.SysFont(font, size)
	
	# create the display surface object
	# score_surface
	score_surface = score_font.render('Score : ' + str(score), True, color)
	
	# create a rectangular object for the text
	# surface object
	score_rect = score_surface.get_rect()
	
	# displaying text
	screen.blit(score_surface, score_rect)

play =True

while play:
    for event in pygame.event.get():		
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    # creating font object my_font
	my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
	game_over_surface = my_font.render(
		'Your Score is : ' + str(score), True, red)
	

	# create a rectangular object for the text
	# surface object
	game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
	game_over_rect.midtop = (window_x/2, window_y/2)
	
	# blit will draw the text on screen
	game_window.blit(game_over_surface, game_over_rect)
	pygame.display.flip()
	
	# after 2 seconds we will quit the program
	time.sleep(3)
	
	# deactivating pygame library
	pygame.quit()
	  
    screen.blit(bg,(0,0))
    
    pygame.display.update()
                
           