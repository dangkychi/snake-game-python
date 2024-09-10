# importing libraries
import pygame
import time
import random
import sys
import turtle

snake_speed = 15

# Window size
window_x=1080
window_y=720

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
bg=pygame.image.load(r'images\bg2.png')
bg=pygame.transform.scale2x(bg)
bgend=pygame.image.load(r'images\bggameover.jfif')
game_window = pygame.display.set_mode((window_x,window_y))


# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [window_x/2-10, window_y/2]

# defining first 4 blocks of snake body
snake_body = [[window_x/2-10, window_y/2],
			[window_x/2-20, window_y/2],
			[window_x/2-30, window_y/2],
			[window_x/2-40, window_y/2]
			]

# defining barrier position
barrier_position =[800,0]
barrier_1_position =[0,130]
# defining barrier
barrier_speed=0
barrier =[[800,0],
		[800,10],
		[800,20],
		[800,30],
		[800,40],
		[800,50],
		[800,60],
		[800,70],
		[800,80],
		[800,90],
		[800,100],
		[800,110],
		[800,120],
		[800,130]
		]

barrier_1 =[[0,130],
		[10,130],
		[20,130],
		[30,130],
		[40,130],
		[50,130],
		[60,130],
		[70,130],
		[80,130],
		[90,130],
		[100,130],
		[110,130],
		[120,130],
		[130,130],
		[140,130],
		[150,130],
		[160,130],
		[170,130],
		[180,130],
		[190,130],
		[190,120],
		[190,110],
		[190,100],
		[190,90],
		[190,80],
		[190,70],
		[190,60],
		[190,50],
		[190,40],
		[190,30],
		[190,20],
		[190,10],
		[190,0]
		]

barrier_2 =[[ 0 ,0]
		]		

# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
				random.randrange(1, (window_y//10)) * 10]
if barrier_position[0] == fruit_position[0] and barrier_position[1] == fruit_position[1]:
	fruit_spawn = False	
if barrier_1_position[0] == fruit_position[0] and barrier_1_position[1] == fruit_position[1]:
	fruit_spawn = False					

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0
highscore = 0

smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('start' , True , green)
text1 = smallfont.render('quit' , True , red)
mouse = pygame.mouse.get_pos()
# if mouse is hovered on a button it
# changes to lighter shade
if window_x/2 <= mouse[0] <= window_x/2+140 and window_y/2 <= mouse[1] <= window_y/2+40:
	pygame.draw.rect(game_window,white,[window_x/2,window_y/2,140,40])
		
else:
	pygame.draw.rect(game_window,black,[window_x/2,window_y/2,140,40])
	
# superimposing the text onto our button
game_window.blit(text , (window_x/2,window_y/2))
	
# updates the frames of the game
pygame.display.update()


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
	game_window.blit(score_surface, score_rect)


#highscore function
def show_highscore(choice,color,font,size):
	highscore_font = pygame.font.SysFont(font, size)
	highscore_surface=highscore_font.render('High Score : ' + str(highscore), True,color)	
	highscore_rect = highscore_surface.get_rect()
	highscore_rect.midtop = (window_x-100,1)
	game_window.blit(highscore_surface,highscore_rect)

#speed function
def show_speed(choice,color,font,size):
	speed_font = pygame.font.SysFont(font, size)
	#speed_surface
	speed_surface=speed_font.render('Speed : ' + str(snake_speed), True,color)	
	speed_rect = speed_surface.get_rect()
	speed_rect.midtop = (window_x/2,1)
	game_window.blit(speed_surface,speed_rect)




#create barrier map
#def barrier_map(x_1,x_2,y_1,y_2):
	#barrier=[[for size1 in range(x_1,x_2,10)],[for size2 in range(y_1,y_2,10)]]


# game over function
def game_over():

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
	time.sleep(5)
	
	# deactivating pygame library
	#pygame.quit()
	

# Main Function
while True:
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()					
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'
		#checks if a mouse is clicked
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			#if the mouse is clicked on the
			# button the game is terminated
			if window_x/2 <= mouse[0] <= window_x/2+140 and window_y/2 <= mouse[1] <= window_y/2+40:
				pygame.quit()
				quit()
		pygame.display.update()		
		# handling key events

	game_window.blit(bg,(0,0))	


	# If two keys pressed simultaneously
	# we don't want snake to move into two
	# directions simultaneously
	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	# Moving the snake
	if direction == 'UP':
		snake_position[1] -= 10
	if direction == 'DOWN':
		snake_position[1] += 10
	if direction == 'LEFT':
		snake_position[0] -= 10
	if direction == 'RIGHT':
		snake_position[0] += 10

	# Snake body growing mechanism
	# if fruits and snakes collide then scores
	# will be incremented by 10
	snake_body.insert(0, list(snake_position))
	if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
		score += 10
		fruit_spawn = False
	else:
		snake_body.pop()

	if not fruit_spawn:
		fruit_position = [random.randrange(1, (window_x//10)) * 10,
					random.randrange(1, (window_y//10)) * 10]
	
	fruit_spawn = True
	
	
	for pos in snake_body:
		pygame.draw.rect(game_window, green,
				pygame.Rect(pos[0], pos[1], 10, 10))
		pygame.draw.rect(game_window, white, pygame.Rect(
			fruit_position[0], fruit_position[1], 10, 10))

		for pos in barrier:
			pygame.draw.rect(game_window, red,
				pygame.Rect(pos[0], pos[1], 10, 10))
		for blockbar in barrier[1:]:
			if snake_position[0] == blockbar[0] and snake_position[1] == blockbar[1]:
				game_over()	
		for pos in barrier_1:
			pygame.draw.rect(game_window, red,
				pygame.Rect(pos[0], pos[1], 10, 10))
		for blockbar in barrier_1[1:]:
			if snake_position[0] == blockbar[0] and snake_position[1] == blockbar[1]:
				game_over()					

	if score > highscore:
		highscore = score
	#change speed snake	
	if score == 50 : 
		snake_speed = 30
	#if score == 100 : 
		#snake_speed = 40
	#if score == 150 :
		#snake_speed = 50
		

	# when out of bounds will be brought to the opposite point
	if snake_position[0] < 0:
		snake_position = [window_x - 10,snake_position[1]]

	if snake_position[0] > window_x-10:
		snake_position = [0 ,snake_position[1]]
		
	if snake_position[1] < 0 :	
		snake_position = [snake_position[0],window_y - 10]

	if snake_position[1] > window_y-10:	
		snake_position = [snake_position[0] , 0]

	# Touching the snake body,game over
	for block in snake_body[1:]:
		if snake_position[0] == block[0] and snake_position[1] == block[1]:
			game_over()

	# displaying score countinuously
	show_score(1, blue, 'times new roman', 20)

	# displaying speed 
	show_speed(1,blue,'times new roman',20)

	# displaying score countinuously
	show_highscore(1, blue, 'times new roman', 20)
	
	# Refresh game screen
	pygame.display.update()

	# Frame Per Second /Refresh Rate
	fps.tick(snake_speed)
