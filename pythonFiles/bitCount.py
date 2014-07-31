"""
A simple function that finds how many bits are inside an integer. The integer
is shifted to the right until it becomes zero and this function returns how
many shifts were made.
"""

def bitCount(num):
    count = 0
    while num > 0:
        if(num and 1 == 1):
            count += 1
        num = num >> 1
    return count
