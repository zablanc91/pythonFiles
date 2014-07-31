"""
Simply reverses the letterings of a string.
"""

def reversal(word):
    if word == None or word == "":
        return word
    else:
        return reversal(word[1:]) + word[0]
