# 20190917 potados

def selection_sort(collection, verbose=False):
	if verbose: print(collection)

	for i in range(0, len(collection) - 1):
		if verbose: print("Rotation " + str(i + 1))

		min_index = i

		# Find the index of the minimum item.
		for j in range(i, len(collection)):
			if collection[j] < collection[min_index]: min_index = j

		# Swap if found something smaller than it has.
		if min_index != i:
			collection[min_index], collection[i] = collection[i], collection[min_index]
			if verbose: print(collection)

def insertion_sort(collection, verbose=False):
	if verbose: print(collection)

	for i in range(0, len(collection) - 1):
		if verbose: print("Rotation " + str(i + 1))

		n = collection[i + 1]

		# From i to zero.
		for j in range(i, -1, -1):
			# Push
			if (n <= collection[j]):
				collection[j + 1] = collection[j]

				# If that was the last push, next loop does not exist.
				# So assign value here.
				if (j == 0): collection[0] = n
				if verbose: print(collection)

			# Assign
			else:
			 	collection[j + 1] = n
				if verbose: print(collection)
				break

def bubble_sort(collection, verbose=False):
	if verbose: print(collection)

	for i in range(0, len(collection) - 1):
		if verbose: print("Rotation " + str(i + 1))

		for j in range(0, len(collection) - 1):
			if (collection[j] > collection[j + 1]):
				collection[j], collection[j + 1] = collection[j + 1], collection[j]
				if verbose: print(collection)
