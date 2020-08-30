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
    
    answer = []
    for i in alphaQuery:
        count = 0
        for j in alphaDict:
            if i == j:
                count += 1
                
        answer.append(count)
    
    return answer

dicti = ['heater', 'cold', 'clod', 'reheat', 'docl']
quer = ['codl', 'heater', 'abcd']
result = stringAnagram(dicti, quer)
print(result)