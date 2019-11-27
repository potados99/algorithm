"""
"""

class State:
    def __init__(self, is_end):
        self.is_end = is_end
        self.transition = {} # dictionary. symbol:destination states.
        self.epsilon_transitions = [] # list. destination states.

    def add_epsilon_transition(self, to_state):
        self.epsilon_transitions.append(to_state)

    def add_transition(self, to_state, symbol):
        self.transition[symbol] = to_state

    def add_next_state(self, next_states, visited):
        if len(self.epsilon_transitions) > 0:
            for state in self.epsilon_transitions:
                if not self in next_states:
                    visited.append(self)
                    state.add_next_state(next_states, visited)
        else:
            next_states.append(self)

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def from_epsilon():
        start_state = State(False)
        end_state = State(True)
        add_epsilon_transition(start_state, end_state)

        return NFA(start_state, end_state)

    @staticmethod
    def from_symbol(symbol):
        start_state = State(False)
        end_state = State(True)
        start_state.add_transition(end_state, symbol)

        return NFA(start_state, end_state)

    @staticmethod
    def from_post_exp(postfix_exp):
        if postfix_exp == "":
            return NFA.from_epsilon()

        stack = []

        for c in postfix_exp:
            if c == '*':
                nfa = stack.pop()
                stack.append(nfa.closure())
            elif c == '|':
                right = stack.pop()
                left = stack.pop()
                stack.append(left.union(right))
            elif c == '.':
                right = stack.pop()
                left = stack.pop()
                stack.append(left.concat(right))
            else:
                nfa = NFA.from_symbol(c)
                stack.append(nfa)

        return stack.pop()

    def concat(self, nfa):
        self.end.add_epsilon_transition(nfa.start)
        self.end.is_end = False

        return NFA(self.start, nfa.end)

    def union(self, nfa):
        start_state = State(False)
        start_state.add_epsilon_transition(self.start)
        start_state.add_epsilon_transition(nfa.start)

        end_state = State(True)
        self.end.add_epsilon_transition(end_state)
        self.end.is_end = False
        nfa.end.add_epsilon_transition(end_state)
        nfa.end.is_end = False

        return NFA(start_state, end_state)

    def closure(self):
        start_state = State(False)
        end_state = State(True)

        start_state.add_epsilon_transition(end_state)
        start_state.add_epsilon_transition(self.start)

        self.end.add_epsilon_transition(end_state)
        self.end.add_epsilon_transition(self.start)
        self.end.is_end = False

        return NFA(start_state, end_state)

class Pattern:
    def __init__(self, infix_exp):
        self.infix_exp = infix_exp

    def parse(self):
        return self.to_postfix(add_explicit_concat)

    def to_postfix(pattern):
        """
        abcd to a.b.c.d to ab.c.d.
        """



        return "ab."

    def add_explicit_concat(pattern):
        """
        (ab)c to (a.b).c
        (a|b)c to (a|b).c
        (b(ca))d to (b.(c.a)).d
        """
        added = ""

        for idx, c in enumerate(pattern):
            if c == '(':
                pass
            elif c == ')':
                if idx >= len(pattern) - 1:
                    break
                if pattern[idx + 1] == ')'
                    continue
                else:
                    added += '.'



    def is_control(c):
        return c == '*' or c == '|' or c == '.'




class Matcher:
    def __init__(self, pattern):
        self.nfa = NFA.from_post_exp(Pattern(pattern).parse())

    def match(self, word):
        current_states = []
        self.nfa.start.add_next_state(current_states, [])

        for c in word:
            next_states = []

            for state in current_states:
                if c in state.transition:
                    state.transition[c].add_next_state(next_states, [])

            current_states = next_states

        return next((x for x in current_states if x.is_end), None) is not None


m = Matcher("a.b")
print(m.match("abcd"))
