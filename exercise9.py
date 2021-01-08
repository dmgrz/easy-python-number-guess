# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random


def compare(x,y):
		if x > y:
			print("Ese no es el numero \t el numero es más chico \n")
		else:
			print("Ese no es el numero \t el numero es más grande \n")
def game():
	i = 0
	intentos_restantes = 3
	game_exit = "exit"
	while i < 3 and i != 3:
		userguess = input("Adivina el numero de 1 - 10: ")
		if userguess == game_exit or userguess == "":
			exit(0)
		else:
			userguess = int(userguess)
		if userguess == guessnumber:
			print("Felicidades, adivinaste el numero!")
			numero_de_intentos = ("En {} intentos ")
			print(numero_de_intentos.format(i + 1))
			i += 1
			break
		else:
			compare(userguess, guessnumber)
			i += 1
			print("Te quedan ", intentos_restantes - 1, "intentos \n")
			intentos_restantes -= 1
guessnumber = random.randint(1,10)



game_exit = "exit"
salir = "continue"

print("Para salir escribe exit o presiona enter. Tenes 3 intentos, buena suerte! ;) \n")

while salir != game_exit:
	if salir == game_exit:
		exit(0)
	elif salir != game_exit:
		game()
		final_number = "El numero era {} \n"
		print(final_number.format(guessnumber))
salir= input()
