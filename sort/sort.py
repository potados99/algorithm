# 20190917 potados

import qsort

def selection_sort(collection, verbose):
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


def insertion_sort(collection, verbose):
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


def bubble_sort(collection, verbose):
	if verbose: print(collection)

	for i in range(0, len(collection) - 1):
		if verbose: print("Rotation " + str(i + 1))
		
		for j in range(0, len(collection) - 1):
			if (collection[j] > collection[j + 1]):
				collection[j], collection[j + 1] = collection[j + 1], collection[j]
				if verbose: print(collection)


def quick_sort_recursive(collection, left, right, verbose):
	if (left < right):
		p = qsort.partition(collection, left, right, verbose)
		quick_sort_recursive(collection, left, p - 1, verbose)
		quick_sort_recursive(collection, p + 1,  right, verbose)


def quick_sort_iterative(collection, verbose, mid_pivot=False, min_partition=0):
	stack = list()

	stack.append(0) # l
	stack.append(len(collection) - 1) # h

	while len(stack) > 0:
		h = stack.pop()
		l = stack.pop()

		if h - l + 1 < min_partition: 
			selection_sort()

		p = qsort.partition(collection, l, h, verbose, mid_pivot)

		# Elements on left
		if l < p - 1:
			stack.append(l)
			stack.append(p - 1)
			
		# Elements on right
		if p + 1 < h:
			stack.append(p + 1)
			stack.append(h)


# Optimize: 0 for none, 1 for partial file, 2 for mid pivot.
def quick_sort(collection, verbose, optimize=0, optmize_arg=0):
	if verbose: print(collection)
	
	quick_sort_iterative(collection, verbose, optimize)

	if verbose: print(collection)
