"""
This function takes a list and puts all individual primitives and variables that
aren't lists into a single list. The function uses recursion to arrive to the
answer.

Example:
>>> dummy = [ [1,2], [3, [4,[5,6]]]]
>>> flattenList(dummy)
[1, 2, 3, 4, 5, 6]
"""
def flattenList(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first = test_list[0]
        rest = test_list[1:]
        return flattenList(first) + flattenList(rest)
    else:
        return [test_list]
