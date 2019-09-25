# 20190926 potados

from util import *
from sort import *
from QuickSort import *

# Print x in iteration and its results as y.
# Useful when drawing a 2D plot in MATLAB.
def dump_result(function, iteration, x_name="", y_name=""):
    x = iteration
    y = map(function, iteration)

    if x_name != "":
        print(x_name + " = " + str(x))

    if y_name != "":
        print(y_name + " = " + str(y))

# This function creates output that can be interpreted by MATLAB.
# Just copy and past the output, MATLAB will show them on plot.
def sorting_test(name, sort_function, data_range):
    dump_result(
        lambda x: elapsed_time(
            lambda: sort_function(random_list(x))
        ),
        data_range,
        "x",
        "y1"
    )
    dump_result(
        lambda x: elapsed_time(
            lambda: sort_function(ordered_list(x))
        ),
        data_range,
        "",
        "y2"
    )
    dump_result(
        lambda x: elapsed_time(
            lambda: sort_function(reverse_ordered_list(x))
        ),
        data_range,
        "",
        "y3"
    )
    print("figure")
    print("plot(x, smoothdata(y1), x, smoothdata(y2), x, smoothdata(y3))")
    print("title('Time Complexity of " + name + "')")
    print("xlabel('Number of Records')")
    print("ylabel('Elapsed Time (millisec)')")
    print("legend({'random data', 'ordered data', 'reverse ordered data'}, 'Location', 'northwest')")
    print("")

x_range = range(1, 1000, 5)
qsorter = QuickSort()

sorting_test("Selection Sort", selection_sort, x_range)

sorting_test("Insertion Sort", insertion_sort, x_range)

sorting_test("Bubble Sort", bubble_sort, x_range)

qsorter.set_optimization(mid_pivot=False, min_partition=0)
sorting_test("Quick Sort Non-Optimized", qsorter.sort, x_range)

qsorter.set_optimization(mid_pivot=True, min_partition=0)
sorting_test("Quick Sort Using Mid Pivot", qsorter.sort, x_range)

qsorter.set_optimization(mid_pivot=False, min_partition=38)
sorting_test("Quick Sort Using Insertion Sort", qsorter.sort, x_range)

qsorter.set_optimization(mid_pivot=True, min_partition=38)
sorting_test("Quick Sort Optimized", qsorter.sort, x_range)
