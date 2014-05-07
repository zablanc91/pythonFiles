"""
This function obtains the permutations or different possible orderings of the
string's characters. Recursively build up the list of permutations by taking out
a character and inserting it into all possible permutations of the rest of
the other characters.

Example:
>>> strPermutation("boat")
['boat', 'bota', 'baot', 'bato', 'btoa', 'btao', 'obat', 'obta', 'oabt', 'oatb', 'otba', 'otab', 'abot', 'abto', 'aobt', 'aotb', 'atbo', 'atob', 'tboa', 'tbao', 'toba', 'toab', 'tabo', 'taob']
"""
#permutation [a,b,c,...] = [a + permutation[b,c,...], b + permutation[a,c,..], ...]

def strPermutation(word):
    if len(word) <= 1:
        return word

    perm_list = []
    for letter in word:
        smallerStr = word.replace(letter, "",1)
        permRest = strPermutation(smallerStr)

        for perm in permRest:
            perm_list.append(letter + perm)
    return perm_list
