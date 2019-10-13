#!/bin/python3

import math
import os
import random
import re
import sys

class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)

def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
    return decorated

# Complete the isBalanced function below.
def isBalanced(s):
    OPENING_PAREN = '('
    CLOSING_PAREN = ')'
    OPENING_CURLY = '{'
    CLOSING_CURLY = '}'
    OPENING_BRACK = '['
    CLOSING_BRACK = ']'
    EMPTY = ''

    @tail_recursive
    def _is_balanced_aux(remaining, pending):
        if remaining == EMPTY:
            return len(pending) == 0

        current = remaining[0]

        if (current == OPENING_PAREN
                or current == OPENING_CURLY
                or current == OPENING_BRACK):
            pending.append(current)

        elif current == CLOSING_PAREN:
            if len(pending) == 0 or pending[-1] != OPENING_PAREN:
                return False
            else:
                pending = pending[:-1]

        elif current == CLOSING_CURLY:
            if len(pending) == 0 or pending[-1] != OPENING_CURLY:
                return False
            else:
                pending = pending[:-1]

        elif current == CLOSING_BRACK:
            if len(pending) == 0 or pending[-1] != OPENING_BRACK:
                return False
            else:
                pending = pending[:-1]

        else:
            raise ValueError

        recurse(remaining[1:], pending)

    return 'YES' if _is_balanced_aux(s, list()) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
