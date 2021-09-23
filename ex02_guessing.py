import random
import math

print("\n-------- CONFIG YOUR GAME -------- \n")

lower = int(input("ENTER LOWER BOUND: "))

upper = int(input("ENTER UPPER BOUND: "))

print("\n--------- START THE GAME --------- \n")

x = random.randint(lower, upper)

print("\nYOU HAVE ONLY", round(math.log(upper - lower + 1, 2)), "CHANCES TO GUESS THE NUMBER!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("GUESS A NUMBER: "))

	if x == guess:
		print("CONGRATULATIONS, YOU DID IT INT ",
			count, " TRY")
		break
	elif x > guess:
		print("TOO SMALL!")
	elif x < guess:
		print("TO HIGH!")

if count >= math.log(upper - lower + 1, 2):
	print("\nTHE NUMBER IS %d" % x)
	print("\nTHE NEXT TIME WILL BE THE RIGHT TIME!\n")