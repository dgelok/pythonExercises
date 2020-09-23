def closest(s, queries):
    # Write your code here
    
    
    def oneguy(query):
        myletter = s[query]
        answers = []
        for i in range(len(s)):
            if s[i] == myletter:
                answers.append(i)
        answers.remove(query)
        if len(answers) == 0:
            return -1
        elif len(answers) == 1:
            return answers[0]
        else:
            ## answers is an array of locations NOT the query.
            dist = []
            for l in answers:
                dist.append(abs(query-l))
            index = dist.index(min(dist))
            return answers[index]



    # x = 5
    # return oneguy(x)

    myAnswers = []
    for l in queries:
        myAnswers.append(oneguy(l))
    return myAnswers

string = "hackerrank"
queries = [4,1,6,8]

print(closest(string, queries))
