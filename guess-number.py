import random
r = random.randint(1,100)
x = 0
while True:
	x += 1
	num = input('Please guess a number:')
	num = int(num)
	if num == r:
		print('Your right!')
		print('Totally guess',x,'times')
		break
	elif num < r:
		print('I want more!')
	elif num > r:
		print('Too much!')

