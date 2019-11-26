"""This module contains a ...

You can run a test using this command:
    python3 -m doctest regex.py -v
or just
    python3 regex.py [--verbose]
"""


# This module can be executed as module and script and by doctest.
if __name__ == "__main__" or __name__ == "regex":
    pass # absolute import
else:
    pass # relative import



class State:
    def __init__(self, is_end):
        self.is_end = is_end
        self.transition = {} # dictionary. symbol:destination states.
        self.epsilon_transitions = [] # list. destination states.


class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def create_state(is_end):
    return State(is_end)


def create_NFA(start_state, end_state):
    return NFA(start_state, end_state)


def add_epsilon_transition(from_state, to_state):
    from_state.epsilon_transitions.append(to_state)


def add_transition(from_state, to_state, symbol):
    from_state.transition[symbol] = to_state


def from_epsilon():
    start_state = create_state(False)
    end_state = create_state(True)
    add_epsilon_transition(start_state, end_state)

    return create_NFA(start_state, end_state)


def from_symbol(symbol):
    start_state = create_state(False)
    end_state = create_state(True)
    add_transition(start_state, end_state, symbol)

    return create_NFA(start_state, end_state)


def concat(first_nfa, second_nfa):
    add_epsilon_transition(first_nfa.end, second_nfa.start)
    first_nfa.end.is_end = False

    return create_NFA(first_nfa.end, second_nfa.start)


def union(first_nfa, second_nfa):
    start_state = create_state(False)
    add_epsilon_transition(start_state, first_nfa.start)
    add_epsilon_transition(start_state, second_nfa.start)

    end_state = create_state(True)
    add_epsilon_transition(first_nfa.end, end_state)
    add_epsilon_transition(second_nfa.end, end_state)
    first_nfa.end.is_end = False
    second_nfa.end.is_end = False

    return create_NFA(start_state, end_state)


def closure(nfa):
    start_state = create_state(False)
    end_state = create_state(True)

    add_epsilon_transition(start_state, end_state)
    add_epsilon_transition(start_state, nfa.start)

    add_epsilon_transition(nfa.end, end_state)
    add_epsilon_transition(nfa.end, nfa.start)
    nfa.end.is_end = False

    return create_NFA(start_state, end_state)


def to_NFA():
    pass


def dump_NFA(nfa):
    dump_state(nfa.start)


def dump_state(state):
    print("State: " + str(state))
    print("    is_end: " + str(state.is_end))
    print("    transition: " + str(state.transition))
    print("    epsilon_transitions: " + str(state.epsilon_transitions))
    print("")

    if len(state.transition) == 0 and len(state.epsilon_transitions) == 0:
        return
    else:
        for tr in state.transition: dump_state(tr)
        for etr in state.epsilon_transitions: dump_state(etr)


def regex(pattern, text, verbose=False):
    """Implementation of regex in Python.

    Args:
        collection (list): Input to sort.
        verbose (bool): Print every rotation if true.

    Returns:
        list: The same as the collection, with sort ascending applied.

    Example:
        blah
    """


    return collection



if __name__ == "__main__":
    state_a = create_state(False)
    state_b = create_state(True)

    add_epsilon_transition(state_a, state_b)
    nfa_a = create_NFA(state_a, state_b)

    state_c = create_state(False)
    state_d = create_state(True)

    add_epsilon_transition(state_c, state_d)
    nfa_b = create_NFA(state_c, state_d)

    nfa_a_and_b = concat(nfa_a, nfa_b)

    dump_NFA(nfa_a_and_b)

    #from common.invoker import from_input
    #from_input(regex)
