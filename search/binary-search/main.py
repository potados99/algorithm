# 20190905 potados

# Search key in the collection and
# return to index of the key if found.
#
# @param collection the ascending sorted integer collection.
# @param key the key to find index.
# @param left the left end of searching range.
# @param right the right end of searching range.
#
# @retirn the index of the key found. -1 if key not found.
def binary_search(collection, key, left, right):
    # Base case.
    if left == right:
        return left

    # Search in progress.
    elif left < right:
        mid_index = int((right + left) / 2)
        if (key < collection[mid_index]):
            return binary_search(collection, key, left, mid_index - 1)
        elif (key > collection[mid_index]):
            return binary_search(collection, key, mid_index + 1, right)
        else:
            return mid_index

    # Not found.
    else:
        return -1

# Wrap binary_search.
# Python does not support overloads.
def binary_search_wrapper(collection, key):
    return binary_search(collection, key, 0, len(collection) - 1)

list = [1, 3, 23, 398, 2923, 9859, 9999, 13435, 68492, 99834]
key = 9999
print(binary_search_wrapper(list, key))
