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
        """
        Add all final states those can be reached with no symbol (epsilon).
        """
        if len(self.epsilon_transitions) > 0:
            for next in self.epsilon_transitions:
                if not next in visited:
                    visited.append(next)
                    next.add_next_state(next_states, visited)
        else:
            next_states.append(self)

    def dump(self):
        print("State: " + str(self))
        print("    is_end: " + str(self.is_end))
        print("    transition: " + str(self.transition))
        print("    epsilon_transitions: " + str(self.epsilon_transitions))

    @staticmethod
    def dump_all(state, iterated=[]):
        if state in iterated: return

        print("State: " + str(state))
        print("    is_end: " + str(state.is_end))
        print("    transition: " + str(state.transition))
        print("    epsilon_transitions: " + str(state.epsilon_transitions))
        print("")

        iterated.append(state)

        if len(state.transition) == 0 and len(state.epsilon_transitions) == 0:
            return
        if state.is_end:
            return
        else:
            for symbol in state.transition:
                State.dump_all(state.transition[symbol], iterated)
            for st in state.epsilon_transitions:
                State.dump_all(st, iterated)

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
                stack.append(stack.pop().closure())
            elif c == '|':
                right = stack.pop()
                left = stack.pop()
                stack.append(left.union(right))
            elif c == '.':
                right = stack.pop()
                left = stack.pop()
                stack.append(left.concat(right))
            else:
                stack.append(NFA.from_symbol(c))

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

    def dump(self):
        print("NFA dump from start: ")
        State.dump_all(self.start)

class Pattern:
    def __init__(self, infix_exp):
        self.infix_exp = infix_exp

    def parse(self):
        return self.to_postfix(self.infix_exp)

    @staticmethod
    def to_postfix(pattern):
        """
        >>> Pattern.to_postfix("(a|b)*c")
        'ab|*c.'
        """
        explicit_pattern = Pattern.add_explicit_concat(pattern)

        stack = []
        postfix_exp = ""

        for c in explicit_pattern:
            if Pattern.is_operator(c):
                preced = Pattern.preced(c)
                while len(stack) != 0 and Pattern.preced(stack[-1]) >= preced:
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

    @staticmethod
    def add_explicit_concat(pattern):
        """
        >>> Pattern.add_explicit_concat("abcd")
        'a.b.c.d'
        >>> Pattern.add_explicit_concat("a(bcd)e")
        'a.(b.c.d).e'
        >>> Pattern.add_explicit_concat("010(-*)((1|2|3|4|5|6|7|8|9|0)*)(-*)((1|2|3|4|5|6|7|8|9|0)*)")
        '0.1.0.(-*).((1|2|3|4|5|6|7|8|9|0)*).(-*).((1|2|3|4|5|6|7|8|9|0)*)'
        """
        added = ""

        for i in range(0, len(pattern) - 1):
            char1 = pattern[i]
            char2 = pattern[i + 1]

            if i == 0: added += char1
            if Pattern.insert_needed(char1, char2): added += '.'

            added += char2

        return added

    @staticmethod
    def insert_needed(char1, char2):
        """
        >>> Pattern.insert_needed('*', 'c')
        True
        >>> Pattern.insert_needed('*', '.')
        False
        >>> Pattern.insert_needed('*', ')')
        False
        >>> Pattern.insert_needed('*', 'c')
        True
        >>> Pattern.insert_needed('a', '*')
        False
        >>> Pattern.insert_needed('a', '.')
        False
        """
        if Pattern.is_char(char1) and Pattern.is_char(char2): return True
        if char1 == ')' and Pattern.is_char(char2): return True
        if Pattern.is_char(char1) and char2 == '(': return True
        if char1 == ')' and char2 == '(': return True
        if char1 == '*' and char2 == '(': return True
        if char1 == '*' and Pattern.is_char(char2): return True
        else: return False

    @staticmethod
    def preced(c):
        if c == '*': return 3
        elif c == '.': return 2
        elif c == '|': return 1
        else: return 0

    @staticmethod
    def is_operator(c): return c == '*' or c == '|' or c == '.'

    @staticmethod
    def is_brace(c): return c == '(' or c == ')'

    @staticmethod
    def is_char(c): return not Pattern.is_operator(c) and not Pattern.is_brace(c)

class Regex:
    def __init__(self, pattern):
        self.infix = pattern
        self.postfix = Pattern(pattern).parse()
        self.nfa = NFA.from_post_exp(self.postfix)

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

    def find(self, word, verbose=False):
        original_states = []
        self.nfa.start.add_next_state(original_states, [])
        current_states = [x for x in original_states]

        index_start = 0

        possible_answers = []

        for idx, c in enumerate(word):
            next_states = []

            for state in current_states:
                if c in state.transition:
                    state.transition[c].add_next_state(next_states, [])

            if len(next_states) == 0:
                if verbose:
                    print("Search will resume from " + str(idx + 1) + "!")
                index_start = idx + 1
                next_states = [x for x in original_states]

            current_states = next_states

            if True in map(lambda st: st.is_end, current_states):
                if verbose:
                    print("Search finished at " + str(idx) + "!")
                    print(word[0:index_start] + "[" + word[index_start:idx+1] + "]" + word[idx+1:])
                possible_answers.append((index_start, idx))

        if len(possible_answers) == 0:
            return None
        else:
            widths = list(map(lambda t: t[1] - t[0], possible_answers))
            index_max_width = widths.index(max(widths))
            return possible_answers[index_max_width]

        return None

    def dump(self):
        print(self)
        print("Matcher for pattern \"" + self.infix + "\".")
        print("NFA:")
        State.dump_all(self.nfa.start)
        pass


if __name__ == "__main__":
    pattern = input("Enter your regex(* . | supported): ")
    matcher = Regex(pattern)

    text = input("Enter some texts to find from: ")

    matched = matcher.match(text)
    print("Does \"" + text + "\" match the pattern \"" + pattern + "\"? " + ("Yes." if matched else "No."))

    if not matched:
        location = matcher.find(text)
        if location is not None:
            print("But pattern is found in the text: " + text[0:location[0]] + "[" + text[location[0]:location[1]+1] + "]" + text[location[1]+1:])
        else:
            print("Pattern is not found in the text!")
