#!/usr/bin/python

import sort

import copy
import time
import random

def random_list(size):
	return [random.randint(1,512) for i in range(size)]
	#return [i for i in range(size, 0, -1)]

def copy_list(origin):
	return copy.deepcopy(origin)

def test(name, body, sample):
	print(name + " started with " + str(len(sample)) + " size of random samples.")
	
	time_bgn = time.time() 
	body(sample)
	elapsed_millis = (time.time() - time_bgn) * 1000.0
	
	print("Time elapsed: " + str(elapsed_millis) + " millisec")
	print(name + " finished.\n")

def test_all(sample_size, verbose=False):
	sample = random_list(sample_size)

	test("Quick sort test", lambda data: sort.quick_sort(data, verbose), copy_list(sample))
	test("Selection sort test", lambda data: sort.selection_sort(data, verbose), copy_list(sample))
	test("Insertion sort test", lambda data: sort.insertion_sort(data, verbose), copy_list(sample))
	test("Bubble sort test", lambda data: sort.bubble_sort(data, verbose), copy_list(sample))


test_all(1000000, verbose=False)
