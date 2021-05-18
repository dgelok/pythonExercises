def scramble(s1, s2):
    mydict = {}
    for i in range (0, len(s1)):
        if s1[i] in mydict:
            mydict[s1[i]] += 1
        else:
            mydict[s1[i]] = 1
    
    for i in range(0, len(s2)):
        if not s2[i] in mydict:
            return False
        elif mydict[s2[i]] <= 0:
            return False
        else:
            mydict[s2[i]] -= 1
    
    return True