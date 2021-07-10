from random import randint
import pygame
from pygame import mixer
import colorama
from colorama import Fore, Style
from os import system
colorama.init(autoreset = True)
pygame.init()
system("title " + "Rock Paper Scissor game by M. Hamza Kashif")
k = 1
tie_Sound = mixer.Sound("tie.wav")
lose_Sound = mixer.Sound("lose.mp3")
win_Sound = mixer.Sound("win.wav")
matchwin_Sound = mixer.Sound("MatchWon.wav")
matchlose_Sound = mixer.Sound("MatchLose.wav")
matchtie_Sound = mixer.Sound("MatchTie.wav")
invalid_Sound = mixer.Sound("invalid.wav")
while k == 1:
	score_player = 0
	score_computer = 0
	rounds = int(input("How many rounds you want: "))
	rounds = rounds + 1
	for i in range(1, rounds, 1):
		print("Round ",i)
		x = int(input('1 for rock, 2 for paper, 3 for scissors: '))
		y = randint(1,3)
		if x == 1 and y == 1:
			print(Fore.BLUE + 'Player: Rock')
			print(Fore.GREEN + 'Computer: Rock')
			print(Fore.CYAN + 'Status: Tie')
			tie_Sound.play()
		elif x == 1 and y == 2:
			print(Fore.BLUE + 'Player: Rock')
			print(Fore.GREEN + "Computer: Paper")
			print(Fore.RED + "Status: Lose")
			lose_Sound.play()
			score_computer = score_computer + 1
		elif x == 1 and y == 3:
			print(Fore.BLUE + 'Player: Rock')
			print(Fore.GREEN + 'Computer: Scissors')
			print(Fore.MAGENTA + 'Status: Win')
			win_Sound.play()
			score_player = score_player + 1
		elif x == 2 and y == 1:
			print(Fore.BLUE + 'Player: Paper')
			print(Fore.GREEN + 'Computer: Rock')
			print(Fore.MAGENTA + "Status: Win")
			win_Sound.play()
			score_player = score_player + 1
		elif x == 2 and y == 2:
			print(Fore.BLUE + 'Player: Paper')
			print(Fore.GREEN + 'Computer: Paper')
			print(Fore.CYAN + 'Status: Tie')
			tie_Sound.play()
		elif x == 2 and y == 3:
			lose_Sound.play()
			print(Fore.BLUE + 'Paper: Paper')
			print(Fore.GREEN + 'Computer: Scissors')
			print(Fore.RED + 'Status: Lose')
			score_computer = score_computer + 1
		elif x == 3 and y == 1:
			lose_Sound.play()
			print(Fore.BLUE + 'Player: Scissors')
			print(Fore.GREEN + 'Computer: Rock')
			print(Fore.RED + "Status: Lose")
			score_computer = score_computer + 1
		elif x == 3 and y == 2:
			print(Fore.BLUE + 'Player: Scissors')
			print(Fore.GREEN + "Computer: Paper")
			print(Fore.MAGENTA + "Status: Win")
			win_Sound.play()
			score_player = score_player + 1
		elif x== 3 and y == 3:
			print(Fore.BLUE + 'Player: Scissors')
			print(Fore.GREEN + "Computer: Scissors")
			print(Fore.CYAN + "Status: Tie")
			tie_Sound.play()
		else:
			print(Fore.RED + "Point deducted for invalid option")
			score_player = score_player - 1
			invalid_Sound.play()
		print(Fore.BLUE + "Your Score: ", score_player)
		print(Fore.GREEN + "Computer Score: ", score_computer)	
		print("-------------------------------------------")
	if score_player > score_computer:
		matchwin_Sound.play()
		print(Fore.BLUE + "Your Score: ",score_player)
		print(Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT + Fore.BLUE + "You Win")
	if score_player == score_computer:
		matchtie_Sound.play()
		print(Fore.BLUE + "Your Score: ",score_player)
		print(Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT + Fore.MAGENTA + "Status: Tie")
	else:
		matchlose_Sound.play()
		print(Fore.BLUE + "Your Score: ",score_player)
		print(Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT + Fore.RED + "You Lose")
	k = int(input("Want another round (1 for yes, 0 for No): "))		
