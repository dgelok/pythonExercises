def high(x):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    xList = x.split()
    scores = []
    for i in xList:
        wordscore = 0
        for j in range(0, len(i)):
            myletter = i[j]
            location = alphabet.index(myletter)
            wordscore += (location - 1)
        scores.append(wordscore)

    myAns = scores.index(max(scores))

    return xList[myAns]


print(high("aa b"))