import pygame
import random
import sys

#Set window 7x6
window = pygame.display.set_mode((700, 600))

#Black and white colours for the board and red, blue colours for pieces, special squares, and end square
black = (0, 0, 0)
white = (255, 255, 255)

red = (255, 0, 0)
blue = (0, 0, 255)

green = (0, 255, 0)

purple = (127, 0, 255)

#Fill window white
window.fill(white)

#The colour of the square
colour = white

#Creating the board
for c in range (0, 7, 1):

	for r in range (0, 6, 1):
		
		#Create the sqaures
		pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
		
		#Update the window
		pygame.display.update()
		
		#Switch between black and white
		if colour == white:
			colour = black
		
		else:
			colour = white

	if colour == white:
			colour = black
		
	else:
		colour = white
	
	#Special Squares
	for x in range (3, 5, 3):
	
		for y in range (0, 6, 1):
			
			spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
	
		#End square
		for x in range (6, 7, 6):
		
			for y in range (5, 6, 5):
			
				pygame.draw.rect(window, purple, (600, 500, 100, 100))

#Keep window open
clock = pygame.time.Clock()

#Player 1

#Draw the red piece
xr = 35
yr = 10
p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
pygame.display.update()

input('\nWelcome player 1. You are the RED piece. Press "Enter" when ready.')

#Player 2

#Draw the blue piece
xb = 35
yb = 60
p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
pygame.display.update()

input('Welcome player 2. You are the BLUE piece. Press "Enter" when ready.')

rules = input("\nWould you like to know the rules (Type yes or no)?")

if rules.upper() == "YES":
	#Rules
	print("______________________________\nRules: \n")
	
	#Who starts
	print("Determining who starts: \nBoth players will roll a dice and the player with the higher roll starts first. If there is a tie, a redo will happen.\n")

	#Play by play
	print('Round by round: \nPlayers will take turns rolling the dice, using "Enter" button, and moving forward depending on the roll. You will be rolling a 10 sided dice.\n')

	#Special blocks
	print("Special squares:\nIf a player lands on any block that is green, the player will go back to the beginning.\n") 

	#Special Rolls
	print("Unlucky rolls? Don't worry! \nIf a player rolls either 1 or 2 on their turn, they will receive an extra roll. \nThis may happen multiple times without restrictions. \n")

	#How to win
	print("First person to get to the purple square will win the game.\n")

	#Start
	input('Now that you know the rules, press "Enter" to start. \n')

else:
	input('\nPress "Enter" to start.')
	
#Player 1
def foo():

	global p1, p2, xr, yr, move, colour
	
	while True:
		
		#Roll dice
		input("\nPlayer 1 roll your dice.")
		roll = random.randint(1, 10)
		move = 0
		
		#If roll higher than two
		if roll > 2:
		
			print(f'You rolled {roll} so you will move up {roll} space(s). \n______________________________')
			
			while move < roll:
			
				#Move square by x amount of squares
				xr += 100 
				
				#Fill window white
				window.fill(white)
				
				#The colour of the square
				colour = white
				
				#Creating the board
				for c in range (0, 7, 1):

					for r in range (0, 6, 1):
						
						#Create the sqaures
						pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
						
						#Switch between black and white
						if colour == white:
						
							colour = black
						
						else:
							colour = white

					if colour == white:
					
							colour = black
						
					else:
					
						colour = white
					
					#Special Squares
					for x in range (3, 5, 3):
					
						for y in range (0, 6, 1):
							
							spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
						#End square
						for x in range (6, 7, 6):
						
							for y in range (5, 6, 5):
							
								pygame.draw.rect(window, purple, (600, 500, 100, 100))
				
				#New square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
				
				move += 1
				
				pygame.display.update()
				pygame.time.delay(20)
				
				#If goes past boundaries
				if xr > 700:
					xr = 35
					yr += 100
				
					#Fill window white
					window.fill(white)
				
					#The colour of the square
					colour = white
				
					#Creating the board
					for c in range (0, 7, 1):

						for r in range (0, 6, 1):
						
							#Create the sqaures
							pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
							
							#Switch between black and white
							if colour == white:
								colour = black
							
							else:
								colour = white

						if colour == white:
							colour = black
							
						else:
							colour = white
					
						#Special Squares
						for x in range (3, 5, 3):
						
							for y in range (0, 6, 1):
								
								spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
						
							#End square
							for x in range (6, 7, 6):
							
								for y in range (5, 6, 5):
								
									pygame.draw.rect(window, purple, (600, 500, 100, 100))
					
				#Draw new square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
					
				pygame.display.update()
				pygame.time.delay(20)
				
				if xr == 635 and yr == 510:
					print("Player 1 wins!")
					quit()
			
			#Turn end	
			if not move < roll:
			
				while move == roll:
					
					#If piece lands on special square	
					if xr == 335:
						
						#Reset back to where it was before
						xr = 35
						yr = 10
						
						#Fill window white
						window.fill(white)
						
						#The colour of the square
						colour = white
						
						#Creating the board
						for c in range (0, 7, 1):

							for r in range (0, 6, 1):
								
								#Create the sqaures
								pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
								
								#Switch between black and white
								if colour == white:
								
									colour = black
								
								else:
									colour = white

							if colour == white:
									colour = black
								
							else:
								colour = white
							
							#Special Squares
							for x in range (3, 5, 3):
							
								for y in range (0, 6, 1):
									
									spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
							
								#End square
								for x in range (6, 7, 6):
							
									for y in range (5, 6, 5):
									
										pygame.draw.rect(window, purple, (600, 500, 100, 100))
							
						#New square
						p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
						p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
						
						pygame.display.update()
						pygame.time.delay(20)
						
						if xr == 635 and yr == 510:
							print("Player 1 wins!")
							quit()
					
					if not xr == 335:
						bar()
		
		#If roll lower than two
		else:
			print(f'You rolled {roll} so you will move up {roll} space(s).\nYou will also get an extra roll.')
			
			while move < roll:
			
				#Move square x amount of times
				xr += 100 
				
				#Fill window white
				window.fill(white)
				
				#The colour of the square
				colour = white
				
				#Creating the board
				for c in range (0, 7, 1):

					for r in range (0, 6, 1):
						
						#Create the sqaures
						pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
						
						#Switch between black and white
						if colour == white:
							colour = black
						
						else:
							colour = white

					if colour == white:
							colour = black
						
					else:
						colour = white
					
					#Special Squares
					for x in range (3, 5, 3):
					
						for y in range (0, 6, 1):
							
							spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
						#End square
						for x in range (6, 7, 6):
						
							for y in range (5, 6, 5):
							
								pygame.draw.rect(window, purple, (600, 500, 100, 100))
				
				#New square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
				
				move += 1
				
				pygame.display.update()
				pygame.time.delay(20)
				
				#If goes past boundaries
				if xr > 700:
					xr = 35
					yr += 100
				
					#Fill window white
					window.fill(white)
				
					#The colour of the square
					colour = white
				
					#Creating the board
					for c in range (0, 7, 1):

						for r in range (0, 6, 1):
							
							#Create the sqaures
							pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
							
							#Switch between black and white
							if colour == white:
								colour = black
							
							else:
								colour = white
	
						if colour == white:
								colour = black
							
						else:
							colour = white
						
						#Special Squares
						for x in range (3, 5, 3):
						
							for y in range (0, 6, 1):
								
								spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
						
							#End square
							for x in range (6, 7, 6):
						
								for y in range (5, 6, 5):
								
									pygame.draw.rect(window, purple, (600, 500, 100, 100))
					
					#New square
					p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
					p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
					
					pygame.display.update()
					pygame.time.delay(20)
				
				#If Player 1 wins		
				if xr == 635 and yr == 510:
					print("Player 1 wins!")
					quit()
				
				#Turn end
				if not move < roll:
					
					while move == roll:
					
						#If piece lands on special square	
						if xr == 335:
						
							#Reset back to where it was before
							xr = 35
							yr = 10
						
							#Fill window white
							window.fill(white)
							
							#The colour of the square
							colour = white
							
							#Creating the board
							for c in range (0, 7, 1):
	
								for r in range (0, 6, 1):
									
									#Create the sqaures
									pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
									
									#Switch between black and white
									if colour == white:
										colour = black
									
									else:
										colour = white
	
								if colour == white:
										colour = black
									
								else:
									colour = white
								
								#Special Squares
								for x in range (3, 5, 3):
								
									for y in range (0, 6, 1):
										
										spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
								
									#End square
									for x in range (6, 7, 6):
								
										for y in range (5, 6, 5):
										
											pygame.draw.rect(window, purple, (600, 500, 100, 100))
							
							#New square
							p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
							p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
						
							pygame.display.update()
							pygame.time.delay(20)
					
						if not xr == 335:
						
							move = 11
#Player 2
def bar():

	global p1, p2, xb, yb, move, colour
	
	while True:
		
		#Roll dice
		input("\nPlayer 2 roll your dice.")
		roll = random.randint(1, 10)
		move = 0
		
		#If roll higher than two
		if roll > 2:
		
			print(f'You rolled {roll} so you will move up {roll} space(s). \n______________________________')
			
			while True:
			
				#Move square by x amount of squares
				xb += 100 
				
				#Fill window white
				window.fill(white)
				
				#The colour of the square
				colour = white
				
				#Creating the board
				for c in range (0, 7, 1):

					for r in range (0, 6, 1):
						
						#Create the sqaures
						pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
						
						#Switch between black and white
						if colour == white:
						
							colour = black
						
						else:
							colour = white

					if colour == white:
					
							colour = black
						
					else:
						colour = white
					
					#Special Squares
					for x in range (3, 5, 3):
					
						for y in range (0, 6, 1):
							
							spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
						#End square
						for x in range (6, 7, 6):
						
							for y in range (5, 6, 5):
							
								pygame.draw.rect(window, purple, (600, 500, 100, 100))
				
				#New square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
			
				move += 1
				
				pygame.display.update()
				pygame.time.delay(20)
				
				#If goes past boundaries
				if xb > 700:
					xb = 35
					yb += 100
				
					#Fill window white
					window.fill(white)
				
					#The colour of the square
					colour = white
				
					#Creating the board
					for c in range (0, 7, 1):

						for r in range (0, 6, 1):
						
							#Create the sqaures
							pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
							
							#Switch between black and white
							if colour == white:
								colour = black
						
							else:
								colour = white
	
						if colour == white:
							colour = black
						
						else:
							colour = white
					
						#Special Squares
						for x in range (3, 5, 3):
						
							for y in range (0, 6, 1):
								
								spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
							#End square
							for x in range (6, 7, 6):
							
								for y in range (5, 6, 5):
								
									pygame.draw.rect(window, purple, (600, 500, 100, 100))
						
				#New Square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
					
				pygame.display.update()
				pygame.time.delay(20)
				
				if xb == 635 and yb == 560:
					print("Player 2 wins!")
					quit()
				
				#Turn end
				if not move < roll:

					while move == roll:
					
						#If piece lands on special square	
						if xb == 335:
						
							#Reset back to where it was before
							xb = 35
							yb = 50
						
							#Fill window white
							window.fill(white)
							
							#The colour of the square
							colour = white
							
							#Creating the board
							for c in range (0, 7, 1):
	
								for r in range (0, 6, 1):
									
									#Create the sqaures
									pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
									
									#Switch between black and white
									if colour == white:
									
										colour = black
									
									else:
										colour = white
	
								if colour == white:
										colour = black
									
								else:
									colour = white
								
								#Special Squares
								for x in range (3, 5, 3):
								
									for y in range (0, 6, 1):
										
										spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
								
									#End square
									for x in range (6, 7, 6):
								
										for y in range (5, 6, 5):
										
											pygame.draw.rect(window, purple, (600, 500, 100, 100))
							
							#New square
							p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
							p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
						
							pygame.display.update()
							pygame.time.delay(20)
					
							if xb == 635 and yb == 560:
								print("Player 2 wins!")
								quit()
						
						if not xb == 335:
							foo()
							
		
		#If roll lower than two
		else:
			print(f'You rolled {roll} so you will move up {roll} space(s).\nYou will also get an extra roll.')
		
			while move < roll:
				
				#Move square x amount of times
				xb += 100 
				
				#Fill window white
				window.fill(white)
				
				#The colour of the square
				colour = white
				
				#Creating the board
				for c in range (0, 7, 1):

					for r in range (0, 6, 1):
						
						#Create the sqaures
						pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
						
						#Switch between black and white
						if colour == white:
							colour = black
						
						else:
							colour = white

					if colour == white:
							colour = black
						
					else:
						colour = white
					
					#Special Squares
					for x in range (3, 5, 3):
					
						for y in range (0, 6, 1):
							
							spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
						#End square
						for x in range (6, 7, 6):
							
							for y in range (5, 6, 5):
							
								pygame.draw.rect(window, purple, (600, 500, 100, 100))
				
				#New Square
				p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
				p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
			
				move += 1
				
				pygame.display.update()
				
				if xb > 700:
					xb = 35
					yb += 100
				
				
					#Fill window white
					window.fill(white)
				
					#The colour of the square
					colour = white
						
					#Creating the board
					for c in range (0, 7, 1):
	
						for r in range (0, 6, 1):
					
							#Create the sqaures
							pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
						
							#Switch between black and white
							if colour == white:
								colour = black
						
							else:
								colour = white
							
								if colour == white:
									colour = black
							
								else:
									colour = white
						
							#Special Squares
							for x in range (3, 5, 3):
						
								for y in range (0, 6, 1):
							
									spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
					
								#End square
								for x in range (6, 7, 6):
								
									for y in range (5, 6, 5):
								
										pygame.draw.rect(window, purple, (600, 500, 100, 100))
						
					#New square
					p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
					p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
					
					pygame.display.update()
					pygame.time.delay(20)
				
				
				#If Player 2 wins
				if xb == 635 and yb == 560:
					print("Player 2 wins!")
					quit()
				
				#Turn end
				if not move < roll:

					while move == roll:
					
						#If piece lands on special square	
						if xb == 335:
						
							#Reset back to where it was before
							xb = 35
							yb = 50
						
							#Fill window white
							window.fill(white)
							
							#The colour of the square
							colour = white
							
							#Creating the board
							for c in range (0, 7, 1):
	
								for r in range (0, 6, 1):
									
									#Create the sqaures
									pygame.draw.rect(window, colour, (c * 100, r * 100, 100, 100))
									
									#Switch between black and white
									if colour == white:
										colour = black
									
									else:
										colour = white
	
								if colour == white:
										colour = black
									
								else:
									colour = white
								
								#Special Squares
								for x in range (3, 5, 3):
								
									for y in range (0, 6, 1):
										
										spcsq = pygame.draw.rect(window, green, (x * 100, y * 100, 100, 100))
								
									#End square
									for x in range (6, 7, 6):
								
										for y in range (5, 6, 5):
										
											pygame.draw.rect(window, purple, (600, 500, 100, 100))
							
							#New square
							p1 = pygame.draw.rect(window, red, (xr, yr, 30, 30))
							p2 = pygame.draw.rect(window, blue, (xb, yb, 30, 30))
						
							pygame.display.update()
							pygame.time.delay(20)
					
						if not xb == 335:
							move = 11
					
#Determine who starts
dws = True
while dws == True:
	p1roll = input("______________________________\nPlayer 1, roll your dice.")
	p1roll = random.randint(1, 10)
	print(f'Player 1 rolled {p1roll}.')

	p2roll = input("\nPlayer 2, roll your dice.")
	p2roll = random.randint(1, 10)
	print(f'Player 2 rolled {p2roll}.')
	
	#If player 1 gets higher roll
	if p1roll > p2roll:
		print("\nPlayer 1 starts first. \n______________________________")
		
		dws = False
		
		foo()
			
	#If player 2 gets higher roll
	elif p1roll < p2roll:
		print("\nPlayer 2 starts first. \n______________________________")
				
		dws = False
		
		bar()
				
	#If a tie
	elif p1roll == p2roll:
		print("\nRedo. \n")
