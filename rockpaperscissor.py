from random import randint
import pygame
from pygame import mixer
import colorama
from colorama import Fore, Style
from os import system
colorama.init(autoreset = True)
pygame.init()
system("title Rock Paper Scissor game by M. Hamza Kashif")
check = True
t = 0
k = '1'
q = 1
tie_Sound = mixer.Sound("tie.wav")
lose_Sound = mixer.Sound("lose.wav")
win_Sound = mixer.Sound("win.wav")
matchwin_Sound = mixer.Sound("MatchWon.wav")
matchlose_Sound = mixer.Sound("MatchLose.wav")
matchtie_Sound = mixer.Sound("MatchTie.wav")
invalid_entry_Sound = mixer.Sound("invalid.wav")
while k == '1':
	score_player = 0
	score_computer = 0
	while t == 0:
		rounds = input("How many rounds you want: ")
		if rounds < '0':
			t = 0
		else:
			break
	roundi = int(rounds)		
	roundi = roundi + 1
	for i in range(1, roundi, 1):
		print("Round ",i)
		while q == 1:
			x = input('1 for rock, 2 for paper, 3 for scissors: ')
			if x == '1':
				break
			elif x == '2':
				break
			elif x == '3':
				break
			else:
				print(Style.BRIGHT + Fore.RED + "Invalid Entry")
				invalid_entry_Sound.play()
				q = 1
		y = randint(1,3)
		if x == '1' and y == 1:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Rock')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Rock')
			print(Style.BRIGHT + Fore.CYAN + 'Status: Tie')
			tie_Sound.play()
		elif x == '1' and y == 2:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Rock')
			print(Style.BRIGHT + Fore.GREEN + "Computer: Paper")
			print(Style.BRIGHT + Fore.RED + "Status: Lose")
			lose_Sound.play()
			score_computer = score_computer + 1
		elif x == '1' and y == 3:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Rock')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Scissors')
			print(Style.BRIGHT + Fore.MAGENTA + 'Status: Win')
			win_Sound.play()
			score_player = score_player + 1
		elif x == '2' and y == 1:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Paper')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Rock')
			print(Style.BRIGHT + Fore.MAGENTA + "Status: Win")
			win_Sound.play()
			score_player = score_player + 1
		elif x == '2' and y == 2:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Paper')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Paper')
			print(Style.BRIGHT + Fore.CYAN + 'Status: Tie')
			tie_Sound.play()
		elif x == '2' and y == 3:
			lose_Sound.play()
			print(Style.BRIGHT + Fore.BLUE + 'Paper: Paper')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Scissors')
			print(Style.BRIGHT + Fore.RED + 'Status: Lose')
			score_computer = score_computer + 1
		elif x == '3' and y == 1:
			lose_Sound.play()
			print(Style.BRIGHT + Fore.BLUE + 'Player: Scissors')
			print(Style.BRIGHT + Fore.GREEN + 'Computer: Rock')
			print(Style.BRIGHT + Fore.RED + "Status: Lose")
			score_computer = score_computer + 1
		elif x == '3' and y == 2:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Scissors')
			print(Style.BRIGHT + Fore.GREEN + "Computer: Paper")
			print(Style.BRIGHT + Fore.MAGENTA + "Status: Win")
			win_Sound.play()
			score_player = score_player + 1
		elif x== '3' and y == 3:
			print(Style.BRIGHT + Fore.BLUE + 'Player: Scissors')
			print(Style.BRIGHT + Fore.GREEN + "Computer: Scissors")
			print(Style.BRIGHT + Fore.CYAN + "Status: Tie")
			tie_Sound.play()
		print(Style.BRIGHT + Fore.BLUE + "Your Score: ", score_player)
		print(Style.BRIGHT + Style.BRIGHT + Fore.GREEN + "Computer Score: ", score_computer)	
		print("-------------------------------------------")
	if score_player > score_computer:
		matchwin_Sound.play()
		print(Style.BRIGHT + Fore.BLUE + "Your Score: ",score_player)
		print(Style.BRIGHT + Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT  + Fore.BLUE + "You Win")
	elif score_player == score_computer:
		matchtie_Sound.play()
		print(Style.BRIGHT + Fore.BLUE + "Your Score: ",score_player)
		print(Style.BRIGHT + Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT + Fore.MAGENTA + "Status: Tie")
	else:
		matchlose_Sound.play()
		print(Style.BRIGHT + Fore.BLUE + "Your Score: ",score_player)
		print(Style.BRIGHT + Fore.GREEN + "Computer Score: ",score_computer)
		print(Style.BRIGHT + Fore.RED + "You Lose")
	k = input("Want another round (1 for yes, 0 for No): ")		
