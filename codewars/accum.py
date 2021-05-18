def accum(s):
    answer = ""
    sLen = len(s)
    for i in range(0, sLen):
        letter = s[i].lower()
        answer += letter.upper() + i * letter
        answer += "-"
    
    answer = answer.rstrip(answer[-1])
    return answer
