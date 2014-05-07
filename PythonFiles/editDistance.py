"""
This function finds the edit distance between two words. The edit distance is
number of inserts, deletes, and replacements of characters needed to be made
on the first word in order to make it appear as the second word. Dynamic
programming is used build up the edit distance of smaller parts of the words
in order to obtain the edit distance of the entire two words.
"""


def editDistance(w1, w2):
    E = []

    for i in range(0, len(w1)+1):
        E.append([i])
    for j in range(1, len(w2)+1):
        E[0].append(j)

    for i in range(1, len(w1)+1):
        for j in range(1, len(w2)+1):
            if w1[i - 1] == w2[j - 1]:
                E[i].append(min(1 + E[i-1][j], 1 + E[i][j-1], E[i-1][j-1]))
            else:
                E[i].append(min(1 + E[i-1][j], 1 + E[i][j-1], 1 + E[i-1][j-1]))
                
    print "The edit distance between " + w1 + " and " + w2 + " is: " + str(E[len(w1)][len(w2)])
        
