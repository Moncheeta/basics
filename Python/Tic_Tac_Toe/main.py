import pygame
import sys
import random

width = 360
height = 360

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Tic Tac Toe")
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont('Arial', 150) 

white = [255, 255, 255]
line_color = [10, 10, 10]

""""
Todo:Check for r pressed to reset
"""

class Tic_Tac_Toe():
	def __init__(self):
		self.player1 = myfont.render('x', False, (0, 0, 0)) #player x
		self.player1_score = 0 #player x score
		self.player2 = myfont.render('o', False, (0, 0, 0)) #player o
		self.player2_score = 0 #player o score
		self.player = self.player1 #current player

		self.turn = 0 #turn 0 = player x while turn 1 = player o
		self.cols = 3 #number of coleums
		self.rows = 3 #number of rows
		self.positions = [[[None for a in range(3)] for b in range(self.rows)] for c in range(self.cols)] #keeps track of what each player placed
		self.check_player = None #lets the main loop know whether x or o got a point
		x_or_o = random.randint(0, 1)
		if x_or_o == 0:
			self.turn = 0
		else:
			self.turn = 1
	def set_positions(self): #resets self.positions
		self.positions = [[[None for a in range(3)] for b in range(self.rows)] for c in range(self.cols)] #keeps track of what each player placed
		self.turn = 0 #resets turn to start with player x

	def take_turn(self): #takes a turn
		if self.turn == 0:
			self.turn = 1
		else:
			self.turn = 0

	def select(self, row, col): #adds a x or o in self.positions
		x_offset = -98
		y_offset = -155
		if row == 0:
			posy = height / 3 + y_offset
		elif row == 1:
			posy = height / 3 * 2 + y_offset
		elif row == 2:
			posy = height + y_offset

		if col == 0:
			posx = width / 3 + x_offset
		elif col == 1:
			posx = width / 3 * 2 + x_offset
		elif col == 2:
			posx = width + x_offset
		if self.turn == 0:
			xoro = 0
		elif self.turn == 1:
			xoro = 1

		if self.positions[row][col][0] == 0 or self.positions[row][col][0] == 1:
			return -1;
		else:
			self.positions[row][col][0] = xoro #item 0 = type
			self.positions[row][col][1] = posx #item 1 = x position
			self.positions[row][col][2] = posy #item 2 = y position
			return 0

	def print_lines(self): #prints the #
		pygame.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
		pygame.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
		pygame.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
		pygame.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)

	def check_pos(self): #checks where the x or o should go depending on mouse position. This is activated when mouse button is down
		x, y = pygame.mouse.get_pos()
		if (x < width / 3):
			col = 0
		elif (x < width / 3 * 2):
			col = 1
		elif (x < width):
			col = 2
		else:
			col = None
		if (y < height / 3):
			row = 0
		elif (y < height / 3 * 2):
			row = 1
		elif (y < height):
			row = 2
		else:
			row = None
		return row, col

	def print_xando(self): #prints the x and o on the screen
		current_row = 0
		for row in self.positions:
			current_col = 0
			for col in row:
				xoro = self.positions[current_row][current_col][0]
				posx = self.positions[current_row][current_col][1]
				posy = self.positions[current_row][current_col][2]
				if xoro == 0:
					self.player = self.player1
					screen.blit(self.player, (posx, posy))
				elif xoro == 1:
					self.player = self.player2
					screen.blit(self.player, (posx, posy))
				elif xoro is None or posx is None or posy is None:
					pass
				else:
					pass
				current_col += 1
			current_row += 1

	def win_check(self): #checks for win
		col = 0
		row_num = 0
		for row in self.positions:
			if self.positions[row_num][0][0] is None or self.positions[row_num][1][0] is None or self.positions[row_num][2][0] is None:
				pass
			else:
				if row[0][0] == row[1][0] == row[2][0]: #checks for filled rows
					if self.positions[row_num][0][0] == 0:
						self.check_player = self.player1
					elif self.positions[row_num][0][0] == 1:
						self.check_player = self.player2
					return True
			row_num += 1
		while col != self.cols:
			if self.positions[0][col][0] is None or self.positions[1][col][0] is None or self.positions[2][col][0] is None:
				pass
			else:
				if self.positions[0][col][0] == self.positions[1][col][0] == self.positions[2][col][0]: #checks for any filled coleums
					if self.positions[0][col][0] == 0:
						self.check_player = self.player1
					elif self.positions[0][col][0] == 1:
						self.check_player = self.player2
					return True
			col += 1
		if self.positions[0][0][0] is None or self.positions[1][1][0] is None or self.positions[2][2][0] is None:
			pass
		else:
			if self.positions[0][0][0] == self.positions[1][1][0] == self.positions[2][2][0]: #checks for a left diagonal
				if self.positions[0][0][0] == 0:
					self.check_player = self.player1
				elif self.positions[0][0][0] == 1:
					self.check_player = self.player2
				return True
		if self.positions[0][2][0] is None or self.positions[1][1][0] is None or self.positions[2][0][0] is None:
			pass
		else:
			if self.positions[0][2][0] == self.positions[1][1][0] == self.positions[2][0][0]: #checks for a right diagonal
				if self.positions[0][2][0] == 0:
					self.check_player = self.player1
				elif self.positions[0][2][0] == 1:
					self.check_player = self.player2
				return True
		no = False
		for row in self.positions: #checks for filled game. If it is filled, no = False
			for thing in row:
				if thing[0] is None:
					no = True
		if no is False:
			return True
		return False

game = Tic_Tac_Toe()

while True:
	clock.tick(60)
	screen.fill(white)
	game.print_lines()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			if game.player1_score > game.player2_score:
				print("Player X won!")
			elif game.player1_score < game.player2_score:
				print("Player O won!")
			else:
				print("Tie")
			print("Player X's Score", game.player1_score)
			print("Player O's Score", game.player2_score)
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			row, col = game.check_pos()
			if row is not None:
				if col is not None:
					yezorno = game.select(row, col)
					if yezorno == -1:
						pass
					else:
						game.take_turn()
	game.print_xando()
	check_for_win = game.win_check()
	if check_for_win is True:
		if game.check_player == game.player1:
			game.player1_score += 1
		elif game.check_player == game.player2:
			game.player2_score += 1
		else:
			pass
		game.check_player = None
		game.set_positions()
	pygame.display.update()
