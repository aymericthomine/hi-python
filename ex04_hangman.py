import random

print("\n--------- START THE GAME --------- \n")

words = ['rainbow', 'music', 'computer', 'science', 'programming',
		'python', 'mathematics', 'cooking', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks', 'sunshine',
        'tennis', 'football', 'happy', 'direction']

word = random.choice(words)


print("FIND THIS WORD:")

guesses = ''

turns = 12

while turns > 0:
	
	failed = 0
	
	for char in word:
		
		if char in guesses:
			print(char)
			
		else:
			print("_")
			
			failed += 1
			

	if failed == 0:
		print("\nYOU WIN!")
		
		print("\nTHE WORD IS: ", word, "\n")
		break
	
	guess = input("\nGUESS A CHARACTER: ")
	
	guesses += guess
	
	if guess not in word:
		
		turns -= 1
		
		print("\nWRONG.")
		
		print("\nYOU HAVE", + turns, 'MORE GUESSES\n')
		
		if turns == 0:
			print("YOU LOOSE.\n")
