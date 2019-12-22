import argparse
import time

def from_input(insert_function, search_function):
    """
    Params:
        void insert_function(str, bool): A function that processes user input.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="print every action", action="store_true")
    parsed = parser.parse_args()

    input_keys = map(lambda x: x.strip(), input("Enter keys separated by a comma: ").split(','))
    search_key = input("Enter key to search: ").strip()

    for key in input_keys:
        insert_function(key, parsed.verbose)

    start = time.perf_counter()
    found = search_function(search_key, parsed.verbose)
    end = time.perf_counter()

    elapsed = end - start

    print("Search finished in {time}s.".format(time=elapsed))
    print("Key is {whether}.".format(whether="found" if found else "not found"))
