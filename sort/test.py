#!/usr/bin/python

from QsortDemo import *
from sort import *
from util import *

def test(name, body, sample):
	print(name + " started with " + str(len(sample)) + " size of random samples.")

	time_bgn = time.time()
	body(sample)
	elapsed_millis = (time.time() - time_bgn) * 1000.0

	print("Time elapsed: " + str(elapsed_millis) + " millisec")
	print(name + " finished.\n")

	return elapsed_millis

def test_all(sample_size, verbose=False):
	sample = random_list(sample_size)

	qsorter = QsortDemo()
	qsorter.set_optimization(mid_pivot=False, min_partition=0)

	test("Pure Quick sort test", lambda data: qsorter.sort(data), copy_list(sample))
	qsorter.set_optimization(mid_pivot=True, min_partition=39)
	test("Optimized quick sort test", lambda data: qsorter.sort(data), copy_list(sample))
	test("Selection sort test", lambda data: selection_sort(data, verbose), copy_list(sample))
	test("Insertion sort test", lambda data: insertion_sort(data, verbose), copy_list(sample))
	test("Bubble sort test", lambda data: bubble_sort(data, verbose), copy_list(sample))

def get_proper_n(n_range):
	# With n_sample different samples
	n_sample = 20

	# With n_measure sortings each
	n_measure = 20

	possible_n = list()
	sorter = QsortDemo()
	sorter.set_optimization(mid_pivot=True, min_partition=0)

	for i in n_range:
		qsort_elapsed = list()
		isort_elapsed = list()

		for _ in range(0, n_sample):
			sample = random_list(i)
			qsort_elapsed.append(average([elapsed_time(lambda data: sorter.sort(data), copy_list(sample)) for x in range(0, n_measure)]))
			isort_elapsed.append(average([elapsed_time(lambda data: insertion_sort(data, False), copy_list(sample)) for x in range(0, n_measure)]))

		gain = average(isort_elapsed) - average(qsort_elapsed)

		if gain > 0:
			print("Quick sort is faster than insertion sort when record is " + str(i))
			possible_n.append(i)

	return min(possible_n)
