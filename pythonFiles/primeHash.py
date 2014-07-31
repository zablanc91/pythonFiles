
"""
Generates a hash code for a given string. First the string is converted to lower
case. Each character is turned into aninteger according to its position in the
alphabet and that value is usedto retrieve a prime number. The hash code is
the product of all these primes.
"""
_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
def primeHash(string):
    string = string.lower()
    result = 1
    for character in string:
        result = result * _prime[ord(character) - 96]
    return result


"""
Tests to see if two words are anagrams by comparing their hash values obtained
from primeHash.
"""
def isAnagram(str1, str2):
    return primeHash(str1) == primeHash(str2)
