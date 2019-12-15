"""This module contains a single function: [blahblah].

You can run a test using this command:
    python3 -m doctest [blahblah].py -v
or just
    python3 [blahblah].py [--verbose]
"""



def create_fsm(pattern, optimize=True, verbose=False):
    """ Create an optimized Finite State Machine.

    Args:
        pattern (string): A string to analyze.

    Returns:
        list: Optimized state machine, in list form.

    Examples:
        >>> create_fsm("10100111", optimize=True)
        [-1, 0, -1, 0, 2, -1, 1, 1]
        >>> create_fsm("10100111", optimize=False)
        [-1, 0, 0, 1, 2, 0, 1, 1]
    """

    # Create FSM(The next array).
    next = [None] * len(pattern)
    lps = -1 # Longest proper prefix
    for current_char_index in range(0, len(pattern)):
        next[current_char_index] = lps
        while (lps >= 0) and (pattern[current_char_index] != pattern[lps]):
            lps = next[lps]
        lps += 1

    # Optimize FSM.
    if optimize:
        for current_char_index in range(0, len(pattern)):
            lps = current_char_index
            while (lps >= 0) and (pattern[current_char_index] == pattern[lps]):
                lps = next[lps]
                next[current_char_index] = lps

    return next


def kmp(text, pattern, verbose=False):
    """
    >>> kmp("ABBBCBABDBEBABBABABA", "ABAB")
    15
    >>> kmp("ABBBCBABDBEBABBABABA", "ABCD")
    -1
    """
    if verbose:
        print("KMP search for a given pattern \"" + pattern + "\" in \"" + text + "\".")

    next = create_fsm(pattern=pattern, optimize=True, verbose=verbose)

    if verbose:
        print("FSM for the pattern: " + str(next))

    current_char_index = 0
    comparisons = 0
    lps = 0

    while current_char_index < len(text) and lps < len(pattern):
        # The inner loop below might be reduced to a single if-statement
        # when the FSM is optimized (No need to keep jumping).

        # Reaching the loop means the condition of the loop above is evaluated for
        # at least one time.
        comparisons += 1

        while (lps >= 0) and (text[current_char_index] != pattern[lps]):
            comparisons += 1
            lps = next[lps]

        current_char_index += 1
        lps += 1

    if lps == len(pattern):
        found_index = current_char_index - len(pattern)
        if verbose:
            print("Pattern found at index " + str(found_index) + ": ", end='')
            print(text[0:found_index] + "[" + pattern + "]" + text[found_index+len(pattern):])
            print(str(comparisons) + " comparisons.")
        return found_index
    else:
        if verbose:
            print("Pattern not found.")
            print(str(comparisons) + " comparisons.")
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)

    kmp("ababacabcbababca", "ababca", verbose=True)
