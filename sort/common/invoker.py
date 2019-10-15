import argparse


def from_input(verbosable_sort_function):
    """Invoke sort function with input data from user's shell.

    The verbosable_sort_function is a function that receives two parameters,
    collection and verbosity, and returns the sorted collection.

    The verbosity is determined by the command line option. If the user set the
    --verbose flag, it will show all steps of the sorting function.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="print every rotation", action="store_true")
    parsed = parser.parse_args()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(verbosable_sort_function(unsorted, parsed.verbose))
