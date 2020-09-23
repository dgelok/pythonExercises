def maximumContainers(scenarios):
    # Write your code here
    inputs = []
    for item in scenarios:
        inputs.append(item.split(" "))
    
    bigDict = {}
    for i in range(len(inputs)):
        bigDict[i] = {
            "n": inputs[i][0],
            "cost": inputs[i][1],
            'm': inputs[i][2]
        }
    
    for i in bigDict:
        obj = bigDict[i]
        cash = int(obj['n'])
        cost = int(obj['cost'])
        refund = int(obj['m'])
        nContainers = 0
        total = 0
        while cash >= cost:
            cash -= cost
            nContainers += 1
            total += 1
        while nContainers >= refund:
            nContainers -= refund
            nContainers += 1
            total += 1
        
        print(total)




x = ['10 2 5', '12 4 4', '6 2 2']
maximumContainers(x)