import random
r = random.randint(1,100)
while True:
	num = input('Please guess a number:')
	num = int(num)
	if num == r:
		print('Your right!')
		break
	elif num < r:
		print('I want more!')
	elif num > r:
		print('Too much!')

