# 20190926 potados

from dump import *
from sort import *
from test import *

# Test all sorting functions.
def test_all(sample_size, verbose=False):
	sample = random_list(sample_size)

	qsorter = QuickSort()
	qsorter.set_optimization(mid_pivot=False, min_partition=0)

	test_elapsed_time("Pure Quick sort test", lambda data: qsorter.sort(data), copy_list(sample))
	qsorter.set_optimization(mid_pivot=True, min_partition=39)
	test_elapsed_time("Optimized quick sort test", lambda data: qsorter.sort(data), copy_list(sample))
	test_elapsed_time("Selection sort test", lambda data: selection_sort(data, verbose), copy_list(sample))
	test_elapsed_time("Insertion sort test", lambda data: insertion_sort(data, verbose), copy_list(sample))
	test_elapsed_time("Bubble sort test", lambda data: bubble_sort(data, verbose), copy_list(sample))
	test_elapsed_time("Shell sort test", lambda data: shell_sort(data, verbose), copy_list(sample))

# Get proper n for quick sort.
def get_proper_n(n_range):
	# With n_sample different samples
	n_sample = 20

	# With n_measure sortings each
	n_measure = 20

	possible_n = list()
	sorter = QuickSort()
	sorter.set_optimization(mid_pivot=True, min_partition=0)

	for i in n_range:
		qsort_elapsed = list()
		isort_elapsed = list()

		for _ in range(0, n_sample):
			sample = random_list(i)
			qsort_elapsed.append(average([elapsed_time(lambda: sorter.sort(copy_list(sample))) for x in range(0, n_measure)]))
			isort_elapsed.append(average([elapsed_time(lambda: insertion_sort(copy_list(sample), False)) for x in range(0, n_measure)]))

		gain = average(isort_elapsed) - average(qsort_elapsed)

		if gain > 0:
			print("Quick sort is faster than insertion sort when record is " + str(i))
			possible_n.append(i)

	return min(possible_n)

# Dump all sorting functions.
def dump_all(x_range):
    qsorter = QuickSort()

    dump_sort_function("Selection Sort", selection_sort, x_range, 60)
    dump_sort_function("Exchange Sort", exchangeSort, x_range, 60)

'''
    dump_sort_function("Selection Sort", selection_sort, x_range)
    dump_sort_function("Insertion Sort", insertion_sort, x_range)
    dump_sort_function("Shell Sort", shell_sort, x_range)
    dump_sort_function("Bubble Sort", bubble_sort, x_range)
    qsorter.set_optimization(mid_pivot=False, min_partition=0)
    dump_sort_function("Quick Sort Non-Optimized", qsorter.sort, x_range)
    qsorter.set_optimization(mid_pivot=True, min_partition=0)
    dump_sort_function("Quick Sort Using Mid Pivot", qsorter.sort, x_range)
    qsorter.set_optimization(mid_pivot=False, min_partition=38)
    dump_sort_function("Quick Sort Using Insertion Sort", qsorter.sort, x_range)
    qsorter.set_optimization(mid_pivot=True, min_partition=38)
    dump_sort_function("Quick Sort Optimized", qsorter.sort, x_range)
'''


#test_all(10)
dump_all(range(1, 1000, 5))
