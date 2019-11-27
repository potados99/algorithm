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

    def dump(self, iterated=[]):
        if self in iterated: return

        print("State: " + str(self))
        print("    is_end: " + str(self.is_end))
        print("    transition: " + str(self.transition))
        print("    epsilon_transitions: " + str(self.epsilon_transitions))
        print("")

        iterated.append(self)

        if len(self.transition) == 0 and len(self.epsilon_transitions) == 0:
            return
        if self.is_end:
            return
        else:
            for symbol in self.transition:
                dump_state(self.transition[symbol], iterated)
            for state in self.epsilon_transitions:
                dump_state(self, iterated)



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
        return self.to_postfix(self.infix_exp)

    def to_postfix(self, pattern):
        explicit_pattern = self.add_explicit_concat(pattern)

        stack = []
        postfix_exp = ""

        for c in explicit_pattern:
            if self.is_operator(c):
                preced = self.preced(c)
                while len(stack) != 0 and self.preced(stack[-1]) >= preced:
                    postfix_exp += stack.pop()
                stack.append(c)
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while len(stack) != 0 and stack[-1] != '(':
                    postfix_exp += stack.pop()
                stack.pop()
            else:
                postfix_exp += c

        while len(stack) != 0:
            postfix_exp += stack.pop()

        return postfix_exp

    def add_explicit_concat(self, pattern):
        added = ""

        for i in range(0, len(pattern) - 1):
            char1 = pattern[i]
            char2 = pattern[i + 1]

            if i == 0: added += char1
            if self.insert_needed(char1, char2): added += '.'

            added += char2

        return added

    def insert_needed(self, char1, char2):
        if self.is_char(char1) and self.is_char(char2): return True
        if char1 == ')' and self.is_char(char2): return True
        if self.is_char(char1) and char2 == '(': return True
        else: return False

    def preced(self, c):
        if c == '*': return 3
        elif c == '.': return 2
        elif c == '|': return 1
        else: return 0

    def is_operator(self, c): return c == '*' or c == '|' or c == '.'
    def is_brace(self, c): return c == '(' or c == ')'
    def is_char(self, c): return not self.is_operator(c) and not self.is_brace(c)

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

    def dump(self):
        pass


m = Matcher("b*c")
print(m.match("bbbc"))
