
def partition(collection, left, right, verbose):
	pivot = collection[right]
	i = left - 1

	for j in range(left, right):
		if collection[j] < pivot:
			i += 1
			collection[i], collection[j] = collection[j], collection[i]
			if verbose: print(collection)

	collection[i + 1], collection[right] = collection[right], collection[i + 1]

	return i + 1
