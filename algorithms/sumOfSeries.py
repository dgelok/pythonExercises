def sumOfAP(a, d, n):
    sum = 0
    i = 0
    while i < n:
        new = a + i*d
        sum += new
        i += 1
    
    mString = str(sum)
    answer = ""
    for i in range(len(mString)):
        answer = mString[i] + answer
    print(answer)

sumOfAP(1,2,5)