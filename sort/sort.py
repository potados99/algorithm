# 20190917 potados

from util import *

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

	for i in range(1, len(collection)):
		if verbose: print("Rotation " + str(i))

		n = collection[i]

		# j from i - 1 to 0.
		for j in range(i - 1, -2, -1):
			if collection[j] <= n: break

			collection[j + 1] = collection[j]
			if verbose: print(collection)

		collection[j + 1] = n

		if verbose: print(collection)

def bubble_sort(collection, verbose=False):
	if verbose: print(collection)

	for i in range(0, len(collection) - 1):
		if verbose: print("Rotation " + str(i + 1))

		for j in range(0, len(collection) - 1):
			if (collection[j] > collection[j + 1]):
				collection[j], collection[j + 1] = collection[j + 1], collection[j]
				if verbose: print(collection)

def shell_sort(collection, verbose=False):
	if verbose: print(collection)

	size = len(collection)
	gap = round_odd(size / 2)
	rotation = 1

	while gap > 0:
		print(gap)
		if verbose: print("Rotation " + str(rotation))

		gap = round_odd(gap)

		# Number of subarrays: gap
		for i in range(0, gap + 1):
			subarray_insertion_sort(collection, i, size - 1, gap, verbose)

		gap = gap >> 1
		rotation += 1

def subarray_insertion_sort(collection, first, last, gap, verbose):
	if verbose:
		print("first: " + str(first) + " last: " + str(last) + " gap:  " + str(gap))
		print(collection)

	rotation = 1

	for i in range(first + gap, last + 1, gap):
		if verbose: print("		Rotation " + str(rotation))

		n = collection[i]

		# j from i - 1 to 0.
		for j in range(i - gap, first - gap - 1, -gap):
			if collection[j] <= n: break

			collection[j + gap] = collection[j]
			if verbose: print(collection)

		collection[j + gap] = n

		if verbose: print(collection)

		rotation += 1
