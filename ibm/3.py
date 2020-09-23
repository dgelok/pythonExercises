def optimalPoint(magic, dist):
    # Write your code here
    
    # loop through all starting points
    ### map to dict the starting point and the ending amount
    ### 

    def test(x):
        
        fuel = 0
        for j in range(len(magic)):
            fuel += magic[x]             
            fuel -= dist[x]
            if fuel < 0:
                return False
            if x == len(magic):
                x = 0  
            
        return True
            

    answer = []
    for i in range(len(magic)):
        # print(i)
        # print(test(i))
        if test(i):
            answer.append(i)

    if len(answer) == 0:
        return -1
    else:
        return min(answer) 

x = [2, 4, 5, 2]
y = [4, 3, 1, 3]
print(optimalPoint(x,y))