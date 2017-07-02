from __future__ import print_function
import os
import random


def clear_screen():
	"""
	This function will clears the screen. 
	"""
	os.system('cls')


def display_board(board):
	"""
	This function will display the board.
	"""
	# clear_screen()
	print('   |   |')
	print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')


def player_input():
	"""
	This function takes in the player input and assign their marker as 'X' or 'O'
	"""
	marker = ''
	while not (marker == 'O' or marker == 'X'):
		marker = raw_input('Player 1: Do you want to be X or O? ').upper()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')


def place_marker(board, marker, position):
	"""
	This function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.
	"""
	board[position] = marker


def win_check(board, mark):
	"""
	This function takes in a board and checks to see if someone has won.
	"""
	return((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
		(board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
		(board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
		(board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
		(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
		(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
		(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
		(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
	"""
	This function returns string of which player went first.
	"""
	if random.randint(0, 1) == 0:
		return 'Player 1'
	else:
		return 'Player 2'


def space_check(board, position):
	"""
	This function returns a boolean indicating whether a space on the board is freely available.
	"""
	return board[position] == ' '


def full_board_check(board):
	"""
	This function checks if the board is full and returns a boolean value. True if full, False otherwise.
	"""
	for i in range(1, 10):
		if space_check(board, i):
			return False
	return True


def player_choice(board):
	"""
	This function asks for a player's next position (as a number 1-9) and then check if its a free position. 
	If it is, then return the position for later use.
	"""
	position = ' '

	while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
		position = raw_input('Choose your next position (1-9): ')

	return int(position)


def replay():
	"""
	This function asks the player if they want to play again and returns True if they do want to play again.
	"""
	return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def main():
	print('************** Welcome to Tic Tac Toe Game! **************')

	while True:
	    # Reset the board
	    theBoard = [' '] * 10
	    player1_marker, player2_marker = player_input()
	    turn = choose_first()
	    print(turn + ' will go first.')
	    game_on = True

	    while game_on:
	        if turn == 'Player 1':
	            # Player1's turn.
	            
	            display_board(theBoard)
	            position = player_choice(theBoard)
	            place_marker(theBoard, player1_marker, position)

	            if win_check(theBoard, player1_marker):
	                display_board(theBoard)
	                print('Congratulations! You have won the game!')
	                game_on = False
	            else:
	                if full_board_check(theBoard):
	                    display_board(theBoard)
	                    print('The game is a draw!')
	                    break
	                else:
	                    turn = 'Player 2'

	        else:
	            # Player2's turn.
	            
	            display_board(theBoard)
	            position = player_choice(theBoard)
	            place_marker(theBoard, player2_marker, position)

	            if win_check(theBoard, player2_marker):
	                display_board(theBoard)
	                print('Player 2 has won!')
	                game_on = False
	            else:
	                if full_board_check(theBoard):
	                    display_board(theBoard)
	                    print('The game is a tie!')
	                    break
	                else:
	                    turn = 'Player 1'

	    if not replay():
	        break


if __name__ == '__main__':
	main()
