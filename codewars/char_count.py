def count(string):

    answer = {}
    for i in range(0, len(string)):
        if string[i] in answer:
            answer[string[i]] += 1
        else:
            answer[string[i]] = 1

    return answer