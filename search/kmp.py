"""This module contains a single function: [blahblah].

You can run a test using this command:
    python3 -m doctest [blahblah].py -v
or just
    python3 [blahblah].py [--verbose]
"""



def create_fsm(pattern):
    """ Create an optimized Finite State Machine.

    Args:
        pattern (string): A string to analyze.

    Returns:
        list: Optimized state machine, in list form.

    Examples:
        >>> create_fsm("10100111")
        [-1, 0, -1, 0, 2, -1, 1, 1]
    """

    # Create FSM.

    i = 1
    j = 0
    l = len(pattern)
    fsm = [0] * l

    while i < l:

        while j < l - i:
            combo = 0

            if pattern[i] == pattern[j]:
                i += 1
                j += 1
                combo += 1
                fsm[j] = combo
            else:
                i += j
                j = 0
                break
        j = 0

        i += 1


    print(fsm)


    # Optimize FSM.





    pass



def kmp(text, pattern):
    pass
