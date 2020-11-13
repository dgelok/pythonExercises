
def multivector(x, y):
    answer = []
    for i in range(len(x)):
        answer.append(x[i]*y[i])
    
    return answer


x = [2,4,5]
y = [2,3,6]

print(multivector(x,y))