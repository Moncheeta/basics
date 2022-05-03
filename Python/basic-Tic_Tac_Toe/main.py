import random

#I just fixed the double tabbing and check for
#proper user input (if it is a number and if it
#is between 1 and 3)

class TicTacToe:
	def __init__(self):
		self.board = []

	def create_board(self):
		for i in range(3):
			row = []
			for j in range(3):
				row.append('-')
			self.board.append(row)

	@staticmethod
	def get_random_first_player():
		return random.randint(0, 1)

	def fix_spot(self, row, col, player):
		if self.board[row][col] == '-':
			self.board[row][col] = player
			return 0
		return -1

	def is_player_win(self, player):
		win = None
		n = len(self.board)
		# checking rows
		for i in range(n):
			win = True
			for j in range(n):
				if self.board[i][j] != player:
					win = False
					break
			if win:
				return win

		for i in range(n):
			win = True
			for j in range(n):
				if self.board[j][i] != player:
					win = False
					break
			if win:
				return win

		win = True
		for i in range(n):
			if self.board[i][i] != player:
				win = False
				break
		if win:
			return win

		win = True
		for i in range(n):
			if self.board[i][n - 1 - i] != player:
				win = False
				break
		return win

	def is_board_filled(self):
		for row in self.board:
			for item in row:
				if item == '-':
					return False
		return True

	@staticmethod
	def swap_player_turn(player):
		return 'X' if player == 'O' else 'O'

	def show_board(self):
		for row in self.board:
			for item in row:
				print(item, end=" ")
			print()

	@staticmethod
	def get_row_col():
		while True:
			try:
				row, col = list(map(int, input("Enter row and column: ").split()))
				if row < 1 or row > 3 or col < 1 or col > 3:
					print("Given row and col are not in range.")
					print()
				else:
					print()
					break
			except:
				print("Please put inputs in a row col format!")
				print()
		return row, col

	def start(self):
		self.create_board()
		player = 'X' if self.get_random_first_player() == 1 else 'O'
		while True:
			print(f"Player {player} turn")
			self.show_board()
			row, col = self.get_row_col()
			if self.fix_spot(row - 1, col - 1, player) == -1:
				pass
			else:
				if self.is_player_win(player):
					print(f"Player {player} wins the game!")
					break
				if self.is_board_filled():
					print("Match Draw!")
					break
				player = self.swap_player_turn(player)
				print()
		self.show_board()

tic_tac_toe = TicTacToe()
tic_tac_toe.start()
