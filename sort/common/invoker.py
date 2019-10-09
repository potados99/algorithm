import argparse

def from_input(verbosable_sort_function):
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="print every rotation", action="store_true")
    parsed = parser.parse_args()

    user_input = input("Enter numbers separated by a comma: ").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(verbosable_sort_function(unsorted, parsed.verbose))
