import random

def winner(player, opponent):
	if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
		(player == 'p' and opponent == 'r'):
		return True

def play():
	user = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
	computer = random.choice(['r', 'p', 's'])
	print(f"Computer: {computer}")

	if user == computer:
		return "It's a tie!"

	if winner(user, computer):
		return "You won!"

	return "You lost!"

print(play())