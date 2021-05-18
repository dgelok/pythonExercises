def duplicate_encode(word):
    word = word.lower()
    mydict = {}
    finalWord = ""
    for i in range (0, len(word)):
        if word[i] in mydict:
            mydict[word[i]] += 1
        else:
            mydict[word[i]] = 1

    for i in range(0, len(word)):
        if mydict[word[i]] > 1:
            finalWord += ")"
        else:
            finalWord += "("

    return finalWord