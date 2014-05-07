def matchCount(word, txt):
    txt = txt.lower()
    wLen = len(word)
    tLen = len(txt)
    count = 0

    i = 0

    while i < (tLen - wLen):
        m = 0
        while (m < wLen) and (txt[i + m] == word[m]):
            m += 1
        if m == wLen:
            count += 1
        i += 1
    print "The word " + word + " has appeared in the text a total of " + str(count) + " times."
            
        
