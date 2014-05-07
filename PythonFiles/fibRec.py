"""
Retrieves the nth fibobnacci recursively. Uses memoization to speed up the
process, as without it the lookup for fib(n-2) repeats work done by the
lookup for fib(n-1).
"""

_privateCache = {}
def fib(n):
    if n in _privateCache:
        return _privateCache[n]
    else:
        if n <= 1:
            _privateCache[n] = n
        else:
            _privateCache[n] = fib(n-1) + fib(n-2)
        return _privateCache[n]
       

    
"""
Prints out the first n fibonacci numbers.
"""
def generateFibs(n):
    return map(fib, range(1,n))

