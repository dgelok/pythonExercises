# def stringAnagram(dictionary, query):
#     # Write your code here
#     answer = []
#     alphaQuery = []
#     alphaDict = []
#     for n in query:
#         alphaItem = ''.join(sorted(n))
#         alphaQuery.append(alphaItem)
    
#     for m in dictionary:
#         alphaDictItem = ''.join(sorted(m))
#         alphaDict.append(alphaDictItem)
    
#     answer = []
#     for i in alphaQuery:
#         count = 0
#         for j in alphaDict:
#             if i == j:
#                 count += 1
                
#         answer.append(count)
    
#     return answer

def stringAnagram(dictionary, query):
    # Write your code here
    answer = []
    alphaQuery = []
    alphaDict = []
    for n in query:
        alphaItem = ''.join(sorted(n))
        alphaQuery.append(alphaItem)
    
    for m in dictionary:
        alphaDictItem = ''.join(sorted(m))
        alphaDict.append(alphaDictItem)
    
    answerDict = {}

    for i in alphaQuery:
        answerDict.update({i: 0})

    for j in alphaDict:
        if j in answerDict:
            answerDict[j] += 1
    
    answer = []
    for l in alphaQuery:
        answer.append(answerDict[l])
    
    return answer

dicti = ['listen', 'tow', 'silent', 'lisent', 'two', 'abc', 'no', 'on']
quer = ['two', 'bca', 'no', 'listen']
result = stringAnagram(dicti, quer)
print(result)