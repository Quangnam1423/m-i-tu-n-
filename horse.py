import pygame , time , numpy , sys

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Knight`s tour!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

movement = [(0 , 0) , (1 , 2) , (0 , 1) , (1 , 3) , (0 , 2) , (1 , 0) ,\
			(2 , 2) , (0 , 3) , (1 , 1) , (2 , 3) , (0 , 4) , (1 , 6) , \
			(0 , 5) , (1 , 7) , (0 , 6) , (1 , 4) , (2 , 6) , (0 , 7) , \
			(1 , 5) , (2 , 7) , (3 , 5) , (2 , 4) , (3 , 2) , (2 , 1) , \
			(3 , 3) , (2 , 5) , (3 , 7) , (4 , 5) , (3 , 4) , (4 , 2) , \
			(3 , 1) , (2 , 0) , (4 , 1) , (3 , 0) , (5 , 1) , (4 , 0) , \
			(5 , 2) , (4 , 4) , (3 , 6) , (5 , 5) , (4 , 7) , (6 , 6) , \
			(7 , 4) , (5 , 3) , (6 , 1) , (5 , 0) , (6 , 2) , (4 , 3) , \
			(6 , 4) , (5 , 6) , (7 , 5) , (5 , 4) , (4 , 6) , (6 , 5) , \
			(5 , 7) , (7 , 6) , (7 , 3) , (7 , 7) , (6 , 7) , (7 , 3) , \
			(6 , 5) , (4 , 6) , (6 , 7) , (5 , 7)
			]

#Knight shape
knight = pygame.image.load('356798155_203600125979216_4041671838877843943_n.png')
knight = pygame.transform.scale(knight, (80,80))
#Background
bg = pygame.image.load('Chessboard480.svg.png')
bg = pygame.transform.scale(bg , (800 , 800))


countdown = 0
x_index = 0
y_index = 0
traverse = 0
running = True
while running:
	#get event
	for event in pygame.event.get():

		if event.type ==pygame.QUIT:
			pygame.quit()
			sys.exit()


	#active
	countdown += 1
	if countdown == 600:
		traverse += 1
		countdown = 0
		if traverse < 64:
			x_index = movement[traverse][0]
			y_index = movement[traverse][1]
		else:
			running = False


	#display for the step

	screen.blit(bg , (0 , 0))
	screen.blit(knight , (x_index * 100 + 10, y_index * 100 + 10))
	pygame.display.update()


		