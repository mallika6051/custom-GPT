from itertools import count

for number in count(start=1, step=2):
	if number > 10:
		break
	print(number)
