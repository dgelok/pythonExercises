
def closest(s, queries):
    # Write your code here
    answers = []
    for num in queries:
        letter = s[num]
        makelist = []
        for i in range(len(s)):
            if s[i] == letter:
                makelist.append(i)
        
        for j in makelist:
            if j == num:
                makelist.remove(j)

        if len(makelist) == 0:
            answers.append(-1)
        elif len(makelist) == 1:
            answers.append(makelist[0])
        else:
            answers.append(0)

    return answers