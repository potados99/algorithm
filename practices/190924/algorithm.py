# 20190924 potados

# Get sum of divisor of given number n.
# This does not include n as divisor.
def divisorSum(n):
	if (n < 1): return 0
	return sum(map(lambda d: d if n % d == 0 else 0, range(1, n)))

# Native number n
def isPerfect(n):
	return divisorSum(n) - n

def isPrime(n):
	return divisorSum(n) == 1

def printNum(n):
	capacity = 1
	count = 0

	for i in range(1, n + 1):
		print i,
		count += 1

		if count >= capacity:
			print ''
			count = 0
			capacity *= 2

# Bubble sort variation.
# Change direction by loop.
def cocktailShaker(collection, verbose=True):
	size = len(collection)
	direction = True # To right

	left = 0
	right = size - 1

	if verbose: print(collection)

	for i in range(0, size / 2 + 1):
		if direction:
			if verbose: print("To right!")
			for j in range(left, size - 1): # 0 to size -1
				if collection[j] > collection[j + 1]:
					collection[j], collection[j + 1] = collection[j + 1], collection[j]
					if verbose: print(collection)
			right -= 1

		else:
			if verbose: print("To left!")
			for j in range(right, 0, -1): # size - 1 to 1
				if collection[j - 1] > collection[j]:
					collection[j - 1], collection[j] = collection[j], collection[j - 1]
					if verbose: print(collection)
			left += 1

		if right - left <= 1:break

		direction = not direction

	if verbose: print(collection)

def exchangeSortReversed(collection, verbose=True):
	size = len(collection)

	for i in range(0, size -1):
		for j in range(i, size):
			if collection[i] < collection[j]:
				collection[i], collection[j] = collection[j], collection[i]
				if verbose: print(collection)
