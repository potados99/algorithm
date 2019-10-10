from util import *


def dump_elapsed_time(name, sorting_function, collection):
    """Measure elapsed time of sorting_function(collection).

    Args:
        name (string): Name of the sorting function.
        sorting_function (list -> list): The sorting function to measure.
        collection (list): Test dataset.
    """
    print(name + " started with " + str(len(sample)) + " size of random samples.")

    time_bgn = time.time()
    sorting_function(sample)
    elapsed_millis = (time.time() - time_bgn) * 1000.0

    print("Time elapsed: " + str(elapsed_millis) + " millisec")
    print(name + " finished.\n")

    return elapsed_millis


def dump_function_xy(function, x_range, x_name="", y_name=""):
    """Dump result of function.

    Get list of y from x_range with each elements passed into function.
    Then print list of x and list of y with given x_name and y_name.

    Args:
        function (int -> int): The function to dump.
        x_range (range): The domain.
        x_name (string): Name of the domain to be printed. if empty, it won't be printed.
        y_name (string): Name of the range to be printed. if empty, it won't be printed.

    Example:
        >>> dump_function_xy(lambda x: x**2, range(0, 5), "x", "y")
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 4, 9, 16]
    """
    x_list = list(x_range)
    y_list = list(map(function, x_list))

    if x_name != "":
        print(x_name + " = " + str(x_list))

    if y_name != "":
        print(y_name + " = " + str(y_list))


def dump_sort_function(name, sort_function, data_range, y_limit=0):
    """Generate a bunch of MATLAB sorce code that draws a 2D plot
    showing a performance of a sort function.

    Invoke dump_funtion_xy for multiple data set to get the relations
    of data and elapsed time, and add some lines for styling the plot.

    Args:
        name (string): Name of the sorting function(algorithm).
        sort_function (list -> list): The sorting function to test.
        data_range (range): How many data to use.
        y_limit (int): High limit of y in the plot.
    """

    print("% " + name + " %")

    dump_function_xy(
        lambda x: elapsed_time(lambda: sort_function(random_list(x))),
        data_range,
        "x",
        "y1"
    )

    dump_function_xy(
        lambda x: elapsed_time(lambda: sort_function(ordered_list(x))),
        data_range,
        "",
        "y2"
    )

    dump_function_xy(
        lambda x: elapsed_time(lambda: sort_function(reverse_ordered_list(x))),
        data_range,
        "",
        "y3"
    )

    print("figure")
    print("plot(x, smoothdata(y1), x, smoothdata(y2), x, smoothdata(y3))")
    print("title('Running time of " + name + "')")
    print("xlabel('Number of Records')")
    print("ylabel('Elapsed Time (millisec)')")
    print("legend({'Random data', 'Ordered data', 'Reverse ordered data'}, 'Location', 'northwest')")
    if y_limit != 0: print("ylim([0 " + str(y_limit) + "])")
    print("")
