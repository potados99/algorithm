#!/usr/bin/python

from QuickSort import *
from sort import *
from util import *

def test_elapsed_time(name, body, sample):
	print(name + " started with " + str(len(sample)) + " size of random samples.")

	time_bgn = time.time()
	body(sample)
	elapsed_millis = (time.time() - time_bgn) * 1000.0

	print("Time elapsed: " + str(elapsed_millis) + " millisec")
	print(name + " finished.\n")

	return elapsed_millis
