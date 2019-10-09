# 20190925 potados

class QuickSort:
	def __init__(self):
		# Use mid index value as a pivot?
		self.mid_pivot = False
		# Use selection sort for array smaller than this.
		self.min_partition = 0

	def partition(self, collection, left, right):
		# Place mid-indexed item at the right end of the collection.
		if self.mid_pivot:
			mid = (left + right) / 2
			collection[mid], collection[right] = collection[right], collection[mid]

		pivot = collection[right]
		i = left - 1

		for j in range(left, right):
			if collection[j] < pivot:
				i += 1
				collection[i], collection[j] = collection[j], collection[i]

		collection[i + 1], collection[right] = collection[right], collection[i + 1]

		return i + 1

	# Insertion sort.
	def small_sort(self, collection, left, right):
		for i in range(left + 1, right + 1):
			n = collection[i]

			# j from i - 1 to 0.
			for j in range(i - 1, -1, -1):
				if collection[j] <= n: break
				collection[j + 1] = collection[j]

			# Handle the special case.
			if j == 0:	collection[0] = n
			else:		collection[j + 1] = n

	# Min_partition 39 recommanded.
	def set_optimization(self, mid_pivot, min_partition):
		self.mid_pivot = mid_pivot
		self.min_partition = min_partition

	# Invoke quick sort for given collection.
	# Optimization level depends on what you gave with set_optimization method.
	def sort(self, collection):
		stack = list()

		stack.append(0)	# l
		stack.append(len(collection) - 1) # h

		while len(stack) > 0:
			h = stack.pop()
			l = stack.pop()

			# No need for partition for subarray of size 1 or 0.
			if l >= h:
				continue

			# Use selection sort for small subarray.
			if h - l + 1 < self.min_partition:
				self.small_sort(collection, l, h)
				continue

			p = self.partition(collection, l, h)

			# Elements on left
			if l < p - 1:
				stack.append(l)
				stack.append(p - 1)

			# Elements on right
			if p + 1 < h:
				stack.append(p + 1)
				stack.append(h)
