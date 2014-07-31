"""
Iteratively finds the nth fibonacci number. A fibonacci number is the sum of the
two previous fibonacci numbers. The zeroth fibonacci number is 0 and the first is
1.
"""

def fib(n):
    if n == 0 or n == 1:
        return n
    prevPrev = 0
    prev = 1
    result = 0

    i = 2
    while i <= n:
        result = prev + prevPrev
        prevPrev = prev
        prev = result
        i += 1
    return result
